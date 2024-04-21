from machine import pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(23))

while True:
  
  sensor.measure()
  temp = sensor.temperature()
  hum = sensor.humidity()
  
  print('Temperature =' temp, 'C')
  print('Humidity =' hum, '%')
  
  sleep(3)

