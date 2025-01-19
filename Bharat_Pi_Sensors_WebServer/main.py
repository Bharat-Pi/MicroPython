import network
import socket
import machine
import dht
import time
import json

# Wi-Fi Credentials
SSID = 'Hotspot'
PASSWORD = 'password'

# User Credentials
USERNAME = "BharatPi"
PASSWORD_USER = "sneha123"
is_authenticated = False

# GPIO Pins for Sensors
DHT_PIN = 5
ULTRASONIC_TRIGGER_PIN = 26
ULTRASONIC_ECHO_PIN = 25
FLOW_SENSOR_PIN = 18

# Initialize Sensors
sensor = dht.DHT22(machine.Pin(DHT_PIN))
ultrasonic_trigger = machine.Pin(ULTRASONIC_TRIGGER_PIN, machine.Pin.OUT)
ultrasonic_echo = machine.Pin(ULTRASONIC_ECHO_PIN, machine.Pin.IN)
flow_sensor = machine.Pin(FLOW_SENSOR_PIN, machine.Pin.IN)

current_sensor = None  # To keep track of the selected sensor


def connect_to_wifi():
    """Connect to Wi-Fi and obtain an IP address."""
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi...")
    start_time = time.time()
    while not station.isconnected():
        if time.time() - start_time > 10:
            raise OSError("Wi-Fi connection failed")
        time.sleep(1)

    print("Connected to Wi-Fi")
    print("IP Address:", station.ifconfig()[0])
    return station.ifconfig()[0]


def read_dht_sensor():
    """Read temperature and humidity from the DHT sensor."""
    try:
        sensor.measure()
        time.sleep(1)
        temp = sensor.temperature()
        hum = sensor.humidity()
        return temp, hum
    except OSError as e:
        print(f"Error reading DHT sensor: {e}")
        return None, None


def read_ultrasonic_sensor():
    """Read distance from the ultrasonic sensor."""
    try:
        ultrasonic_trigger.off()
        time.sleep_us(2)
        ultrasonic_trigger.on()
        time.sleep_us(10)
        ultrasonic_trigger.off()

        while ultrasonic_echo.value() == 0:
            start_time = time.ticks_us()

        while ultrasonic_echo.value() == 1:
            end_time = time.ticks_us()

        duration = end_time - start_time
        distance = (duration / 2) / 29.1  # cm
        return round(distance, 2)
    except Exception as e:
        print(f"Error reading ultrasonic sensor: {e}")
        return None


def read_flow_sensor():
    """Read flow sensor data."""
    try:
        pulse_count = 0

        def count_pulse(pin):
            nonlocal pulse_count
            pulse_count += 1

        flow_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=count_pulse)
        time.sleep(1)  # Measure flow for 1 second
        flow_rate = pulse_count * 2.25  # Convert to liters/min
        return round(flow_rate, 2)
    except Exception as e:
        print(f"Error reading flow sensor: {e}")
        return None


def login_page():
    """Return HTML for the login page."""
    html = """<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: Arial; text-align: center; background-color: #f0f0f0; margin: 0; padding: 0; }
    h2 { color: #1E90FF; margin-top: 60px; font-size: 1.8rem; }  
    form { margin-top: 50px; }
    input { margin: 10px; padding: 10px; font-size: 1rem; width: 25%; }  
    button { padding: 10px 20px; font-size: 1rem; background-color: #4CAF50; color: white; border: none; border-radius: 5px; }
    button:hover { background-color: #45a049; }
    .input-container { margin-bottom: 20px; }
    .logo { margin-top: 30px; margin-bottom: 50px; } 
  </style>
</head>
<body>
  <div class="logo">
    <img src="https://th.bing.com/th/id/OIP.OeBZN8kpKLxoRgidMScltwAAAA?w=179&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7" alt="Bharat Pi Logo" width="100px">
  </div>
  <h2>Welcome to Bharat Pi</h2>
  <form method="POST" action="/login">
    <div class="input-container">
      <input type="text" name="username" placeholder="Username" required><br>
    </div>
    <div class="input-container">
      <input type="password" name="password" placeholder="Password" required><br>
    </div>
    <div class="input-container">
      <button type="submit">Login</button>
    </div>
  </form>
</body>
</html>"""
    return html



def sensor_selection_page():
    """Return HTML for the sensor selection page."""
    html = """<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: Arial; text-align: center; background-color: #ADD8E6; margin: 0; padding: 0; }
    h2 { color: #1E90FF; margin-top: 60px; font-size: 1.8rem; }
    form { margin-top: 50px; }
    select { margin: 10px; padding: 10px; font-size: 1rem; }
    button { padding: 10px 20px; font-size: 1rem; background-color: #4CAF50; color: white; border: none; border-radius: 5px; }
    button:hover { background-color: #45a049; }
  </style>
</head>
<body>
  <h2>Select a Sensor</h2>
  <form method="POST" action="/select-sensor">
    <select name="sensor">
      <option value="dht">DHT22 (Temperature & Humidity)</option>
      <option value="ultrasonic">Ultrasonic Sensor(Distance)</option>
      <option value="flow">Flow Sensor(Flow Rate)</option>
    </select><br>
    <button type="submit">Select</button>
  </form>
</body>
</html>"""
    return html


def sensor_data_page(data, chart_data=None, chart_label=None):
    """Return HTML for displaying the selected sensor's data with auto-updating feature."""
    chart_data = chart_data or []
    chart_label = chart_label or "Data"
    
    html = f"""<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body {{ font-family: Arial; text-align: center; background-color: #ADD8E6; }}
    h2 {{ color: #1E90FF; font-size: 2rem; }}
    p {{ font-size: 1.5rem; }}
    canvas {{ max-width: 100%; width: 60%; height: 100px; margin: auto; }}
  </style>
</head>
<body>
  <h2>Sensor Server</h2>
  <p id="sensorData">{data}</p>
  <canvas id="sensorChart"></canvas>
  <script>
    const ctx = document.getElementById('sensorChart').getContext('2d');
    let chart = new Chart(ctx, {{
        type: 'line',
        data: {{
            labels: {list(range(len(chart_data)))},
            datasets: [{{
                label: '{chart_label}',
                data: {chart_data},
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2,
                fill: true,
            }}]
        }},
        options: {{
            responsive: true,
            scales: {{
                x: {{
                    title: {{
                        display: true,
                        text: 'Measurement Number'
                    }}
                }},
                y: {{
                    title: {{
                        display: true,
                        text: '{chart_label}'
                    }}
                }}
            }}
        }}
    }});

    function updateSensorData() {{
      fetch('/sensor-data')
        .then(response => response.text())
        .then(html => {{
          const parser = new DOMParser();
          const newDoc = parser.parseFromString(html, 'text/html');
          const newSensorData = newDoc.getElementById('sensorData').innerText;
          document.getElementById('sensorData').innerText = newSensorData;

          // Update the chart data dynamically without refreshing the page
          const newChartData = JSON.parse(newDoc.getElementById('newChartData').innerText);
          chart.data.datasets[0].data = newChartData;
          chart.update();
        }})
        .catch(err => console.error('Error updating sensor data:', err));
    }}

    setInterval(updateSensorData, 3000); // Update every 3 seconds
  </script>
  <div id="newChartData" style="display:none;">{json.dumps(chart_data)}</div>
</body>
</html>"""
    return html




def handle_request(request):
    """Handle incoming HTTP requests."""
    global is_authenticated, current_sensor

    try:
        request_line = request.split('\r\n')[0]
        method, path, _ = request_line.split()

        if method == "POST" and path == "/login":
            body = request.split("\r\n\r\n")[1]
            params = dict(param.split("=") for param in body.split("&"))
            if params.get("username") == USERNAME and params.get("password") == PASSWORD_USER:
                is_authenticated = True
                return "HTTP/1.1 302 Found\nLocation: /select-sensor\n\n", None
            else:
                return "HTTP/1.1 401 Unauthorized\nContent-Type: text/html\n\nInvalid credentials.", None

        if not is_authenticated:
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", login_page()

        if method == "GET" and path == "/select-sensor":
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", sensor_selection_page()

        if method == "POST" and path == "/select-sensor":
            body = request.split("\r\n\r\n")[1]
            current_sensor = dict(param.split("=") for param in body.split("&")).get("sensor")
            return "HTTP/1.1 302 Found\nLocation: /sensor-data\n\n", None

        if method == "GET" and path == "/sensor-data":
            chart_data = []
            if current_sensor == "dht":
                temp, hum = read_dht_sensor()
                data = f"Temperature: {temp} °C, Humidity: {hum} %"
                chart_data = [temp, hum]
                chart_label = "Temperature (°C)"
                chart_lable = "Humidity (%)"
            elif current_sensor == "ultrasonic":
                distance = read_ultrasonic_sensor()
                data = f"Distance: {distance} cm"
                chart_data = [distance]
                chart_label = "Distance (cm)"
            elif current_sensor == "flow":
                flow = read_flow_sensor()
                data = f"Flow Rate: {flow} L/min"
                chart_data = [flow]
                chart_label = "Flow Rate (L/min)"
            else:
                data = "No sensor selected."
                chart_label = "No Data"

            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", sensor_data_page(data, chart_data, chart_label)

        return "HTTP/1.1 404 Not Found\nContent-Type: text/html\n\nPage not found.", None

    except Exception as e:
        print(f"Error handling request: {e}")
        return "HTTP/1.1 500 Internal Server Error\nContent-Type: text/html\n\nServer Error.", None


# Main Code
try:
    ip_address = connect_to_wifi()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print(f"Server running on http://{ip_address}")

    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")
        request = conn.recv(1024).decode()
        print(f"Request: {request}")

        status, response = handle_request(request)
        conn.send(status.encode())
        if response:
            conn.send(response.encode())
        conn.close()

except Exception as e:
    print(f"Error: {e}")

