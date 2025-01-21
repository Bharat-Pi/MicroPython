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

# GPIO Pin for DHT22 Sensor
DHT_PIN = 18
sensor = dht.DHT22(machine.Pin(DHT_PIN))


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


def read_sensor():
    """Read temperature and humidity from the DHT sensor."""
    try:
        sensor.measure()
        time.sleep(1)
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Sensor Reading - Temperature: {temp} °C, Humidity: {hum} %")
        return temp, hum
    except OSError as e:
        print(f"Error reading sensor: {e}")
        return None, None


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


def web_page(temp, hum):
    """Return HTML for the temperature and humidity data page with units and real-time graph."""
    html = f"""<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet"> <!-- Font Awesome CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- Chart.js CDN -->
  <style>
    html {{ font-family: Arial; text-align: center; background-color: #ADD8E6; }}
    h2 {{ font-size: 3.0rem; color: #1E90FF; }}  /* Blue color for Bharat Pi text */
    p {{ font-size: 2.0rem; }}
    .icon {{ font-size: 2.5rem; margin-right: 10px; vertical-align: middle; }}
    .temp-icon {{ color: #FF4500; }} /* Orange color for temperature icon */
    .hum-icon {{ color: #4682B4; }}  /* Steel blue color for humidity icon */
    .chart-container {{ display: flex; justify-content: center; gap: 30px; margin-top: 20px; }}
    canvas {{ width: 550px !important; height: 280px !important; }}
  </style>
  <script>
    let tempData = [];
    let humData = [];
    let labels = [];

    function updateData() {{
      fetch('/data')
        .then(response => response.json())
        .then(data => {{
          const now = new Date();
          labels.push(now.toLocaleTimeString());
          tempData.push(data.temp);
          humData.push(data.hum);

          if (labels.length > 10) {{
            labels.shift();
            tempData.shift();
            humData.shift();
          }}

          tempChart.update();
          humChart.update();

          document.getElementById("temp").innerHTML = data.temp + " &deg;C";
          document.getElementById("hum").innerHTML = data.hum + " %";
        }});
    }}

    setInterval(updateData, 3000); // Update every 3 seconds

    let tempChart, humChart;

    window.onload = function() {{
      const ctxTemp = document.getElementById('tempChart').getContext('2d');
      tempChart = new Chart(ctxTemp, {{
        type: 'line',
        data: {{
          labels: labels,
          datasets: [{{
            label: 'Temperature (°C)',
            backgroundColor: 'rgba(255, 69, 0, 0.2)',
            borderColor: '#FF4500',
            data: tempData,
          }}]
        }},
        options: {{
          responsive: true,
          scales: {{
            x: {{ title: {{ display: true, text: 'Time' }} }},
            y: {{ title: {{ display: true, text: 'Temperature (°C)' }} }}
          }}
        }}
      }});

      const ctxHum = document.getElementById('humChart').getContext('2d');
      humChart = new Chart(ctxHum, {{
        type: 'line',
        data: {{
          labels: labels,
          datasets: [{{
            label: 'Humidity (%)',
            backgroundColor: 'rgba(70, 130, 180, 0.2)',
            borderColor: '#4682B4',
            data: humData,
          }}]
        }},
        options: {{
          responsive: true,
          scales: {{
            x: {{ title: {{ display: true, text: 'Time' }} }},
            y: {{ title: {{ display: true, text: 'Humidity (%)' }} }}
          }}
        }}
      }});
    }};
  </script>
</head>
<body>
  <h2>Bharat Pi DHT22 Server</h2>
  <p><i class="fas fa-thermometer-half icon temp-icon"></i> Temperature: <span id="temp">{temp} &deg;C</span></p>
  <p><i class="fas fa-tint icon hum-icon"></i> Humidity: <span id="hum">{hum} %</span></p>
  <div class="chart-container">
    <canvas id="tempChart"></canvas>
    <canvas id="humChart"></canvas>
  </div>
</body>
</html>"""
    return html



def data_page():
    """Return JSON data of the temperature and humidity readings."""
    temp, hum = read_sensor()
    response = {'temp': temp if temp is not None else "Error",
                'hum': hum if hum is not None else "Error"}
    return json.dumps(response)


def handle_request(request):
    """Handle incoming HTTP requests."""
    global is_authenticated

    try:
        # Parse the request
        request_line = request.split('\r\n')[0]
        method, path, _ = request_line.split()

        # Handle login POST request
        if method == "POST" and path == "/login":
            body = request.split("\r\n\r\n")[1]
            params = dict(param.split("=") for param in body.split("&"))
            if params.get("username") == USERNAME and params.get("password") == PASSWORD_USER:
                is_authenticated = True
                return "HTTP/1.1 302 Found\nLocation: /\n\n", None
            else:
                return "HTTP/1.1 401 Unauthorized\nContent-Type: text/html\n\nInvalid credentials.", None

        # If not authenticated, show login page
        if not is_authenticated:
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", login_page()

        # Handle sensor data JSON request
        if method == "GET" and path == "/data":
            return "HTTP/1.1 200 OK\nContent-Type: application/json\n\n", data_page()

        # Default: show sensor data page
        temp, hum = read_sensor()
        return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", web_page(temp, hum)

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
