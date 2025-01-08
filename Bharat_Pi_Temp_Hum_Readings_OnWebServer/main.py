/*************************************************************************
   PROJECT NAME:  Bharat Pi Dht11 Sample Code of temp &hum readings on webServer
   AUTHOR: Bharat Pi
   CREATED DATE: 11/11/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.0.1

   DESCRIPTION: This script will give you the sample testing of dht11 sensor,
   which gives you the temperature and humidity reading values on the web server.
                                   
   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   11/11/2024 -    0.0.1       -    Initial release of dht11 sensor sample script to read the data on webserver(Used Thonny IDE application).

 ************************************************************************/

import network
import socket
import machine
import dht
import time
import json

# Wi-Fi Credentials
SSID = 'your ssid'
PASSWORD = 'your password'

# User Credentials
USERNAME = "BharatPi"
PASSWORD_USER = "sneha123"
is_authenticated = False

# GPIO Pin for DHT11 Sensor
sensor = dht.DHT11(machine.Pin(23))

def connect_to_wifi():
    """Connect to Wi-Fi and obtain an IP address."""
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi...")
    start_time = time.time()
    while not station.isconnected():
        if time.time() - start_time > 30:
            print("Failed to connect after 30 seconds")
            raise OSError("Wi-Fi connection failed")
        time.sleep(1)

    print("Connected to Wi-Fi")
    print("IP Address:", station.ifconfig()[0])
    return station.ifconfig()[0]

def read_sensor():
    """Read temperature and humidity from the DHT11 sensor."""
    try:
        sensor.measure()
        time.sleep(1)
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")

        if isinstance(temp, int) and isinstance(hum, int):
            return temp, hum
        else:
            return None, None
    except OSError as e:
        print("Error reading sensor:", e)
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
    """Return HTML for the temperature and humidity data page with units and auto-updating feature."""
    html = f"""<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet"> <!-- Font Awesome CDN -->
  <style>
    html {{ font-family: Arial; text-align: center; background-color: #ADD8E6; }}
    h2 {{ font-size: 3.0rem; color: #1E90FF; }}  /* Blue color for Bharat Pi text */
    p {{ font-size: 2.5rem; }}
    .units {{ font-size: 1.2rem; }}
    .dht-labels{{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }}
    .icon {{ font-size: 2.5rem; margin-right: 10px; vertical-align: middle; }}
    .temp-icon {{ color: #FF4500; }} /* Orange color for temperature icon */
    .hum-icon {{ color: #4682B4; }}  /* Steel blue color for humidity icon */
    .data-value {{ font-size: 2.0rem; }} 
  </style>
  <script>
    function updateData() {{
      fetch('/data')
        .then(response => response.json())
        .then(data => {{
          document.getElementById("temp").innerHTML = "" + data.temp + " &deg;C";
          document.getElementById("hum").innerHTML = "" + data.hum + " %";
        }});
    }}

    setInterval(updateData, 3000); // Update every 3 seconds
  </script>
</head>
<body>
  <h2>Bharat Pi DHT11 Server</h2>
  <p><i class="fas fa-thermometer-half icon temp-icon"></i> Temperature: <span id="temp">{temp} &deg;C</span></p>
  <p><i class="fas fa-tint icon hum-icon"></i> Humidity: <span id="hum">{hum} %</span></p>
</body>
</html>"""
    return html

def data_page():
    """Return JSON data of the temperature and humidity readings."""
    temp, hum = read_sensor()
    if temp is not None and hum is not None:
        response = {'temp': temp, 'hum': hum}
    else:
        response = {'temp': 'Error', 'hum': 'Error'}
    return json.dumps(response)

def handle_request(request):
    """Handle incoming HTTP requests."""
    global is_authenticated

    if b"POST /login" in request:
        content = request.decode()
        body = content.split("\r\n\r\n")[1]
        params = dict(param.split("=") for param in body.split("&"))
        
        # Debug: Print the extracted params to see the values being passed
        print("Extracted parameters:", params)
        
        # Check if username and password are correct
        if params.get("username") == USERNAME and params.get("password") == PASSWORD_USER:
            is_authenticated = True
            return "HTTP/1.1 302 Found\nLocation: /\n\n", None
        else:
            return "HTTP/1.1 401 Unauthorized\nContent-Type: text/html\n\nInvalid credentials.", None

    # If not authenticated, return the login page
    if not is_authenticated:
        return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", login_page()

    # Handle the /data request
    if b"GET /data" in request:
        return "HTTP/1.1 200 OK\nContent-Type: application/json\n\n", data_page()

    # Default response (web page with sensor data)
    temp, hum = read_sensor()
    return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n", web_page(temp, hum)

# Main Code
try:
    ip_address = connect_to_wifi()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print("Server running on http://%s" % ip_address)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % str(request))

        status, response = handle_request(request)
        conn.send(status.encode())
        if response:
            conn.sendall(response.encode())
        conn.close()
except Exception as e:
    print("Error:", e)


