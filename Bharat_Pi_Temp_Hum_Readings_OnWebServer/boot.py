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
# upload this boot.py file first then, upload the main.py file to board and run the programme.(main.py file is available in this folder only)

import network
import time

# Reset the interface
station = network.WLAN(network.STA_IF)
station.active(False)  
time.sleep(1)
station.active(True)  

ssid = 'your ssid here'
password = 'your password here'

# Connect to the network
station.connect(ssid, password)

# Wait for the connection
start_time = time.time()
while not station.isconnected():
    if time.time() - start_time > 10:
        print("Connection failed")
        raise OSError("Wi-Fi connection failed")
    time.sleep(1)

print("Connection successful")
print(station.ifconfig())
