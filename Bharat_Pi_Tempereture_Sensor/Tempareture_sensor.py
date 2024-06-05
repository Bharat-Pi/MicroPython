/*************************************************************************
   PROJECT: Bharat Pi Tempereture and Humidity sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing of tempereture and humidity sensor,
   which will measures the tempereture and humidty
   and gives the respective values as output when you run the code.
   #the data pin will be 23
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/

from machine import Pin
from time import sleep
import dht
 
sensor = dht.DHT11(Pin(23))
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
 
    print('Temperature=', temp, 'C')
    print('Humidity=', hum, '%')
 
    sleep(3)
