/*************************************************************************
   
   PROJECT NAME: Bharat Pi Tempereture and Humidity sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of tempereture and humidity sensor,
   which will measures the tempereture and humidty
   and gives the respective values as output when you run the code.
   #PIN CONNECTIONS
   VCC   -   3.3V
   DATA   -   23
   GND   -   GND

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of tempereture and humidity sensor sample script to read the data(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

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
