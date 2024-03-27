#pin connections 
#1 to 3.3V
#2 to 14 (ANY GPIO)
#4 to GND

from machine import pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))

while True::
  
  sensor.measure()
  temp = sensor.temperature()
  hum = sensor.humidity()
  print('Temperature: %2.2f C' %temp)
  print('Humidity: %2.2f %%' %humidity)
  sleep(1)

