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
# After uploading the boot.py file then, upload this main.py file to board and run.(boot.py file is available in this folder only)

import socket
import machine
import dht
import time
import json

#Replace your GPIO pin here
sensor = dht.DHT11(machine.Pin(23))

def read_sensor():
    try:
        sensor.measure()
        time.sleep(1)
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")
        
        if (isinstance(temp, int) and isinstance(hum, int)):
            hum = round(hum, 2)
            return temp, hum
        else:
            return None, None
    except OSError as e:
        print("Error reading sensor:", e)
        return None, None

def web_page(temp, hum):
    html = """<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
      font-family: Arial;
      display: inline-block;
      margin: 0px auto;
      text-align: center;
      background-color: #ADD8E6;
    }
    h2 { font-size: 3.0rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 1.2rem; }
    .dht-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
</head>
<body>
  <h2>Bharat Pi DHT Server</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="dht-labels">Temperature</span> 
    <span id="temperature">Loading...</span>
    <sup class="units">&deg;C</sup>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="dht-labels">Humidity</span>
    <span id="humidity">Loading...</span>
    <sup class="units">%</sup>
  </p>

  <script>
    setInterval(function() {
      fetch('/data')
        .then(response => response.json())
        .then(data => {
          document.getElementById('temperature').innerHTML = data.temp;
          document.getElementById('humidity').innerHTML = data.hum;
        })
        .catch(err => {
          console.error('Error fetching data:', err);
        });
    }, 3000);
  </script>
</body>
</html>"""
    return html

def data_page():
    temp, hum = read_sensor()
    if temp is not None and hum is not None:
        response = {
            'temp': temp,
            'hum': hum
        }
    else:
        response = {
            'temp': 'Error',
            'hum': 'Error'
        }
    return json.dumps(response)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))

    if b'GET /data' in request:
        response = data_page() 
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: application/json\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response.encode())
    else:
        temp, hum = read_sensor()
        response = web_page(temp, hum) 
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response.encode())

    conn.close()
