
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
