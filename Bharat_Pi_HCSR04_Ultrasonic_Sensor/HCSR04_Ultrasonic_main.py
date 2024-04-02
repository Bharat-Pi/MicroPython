#PIN CONNECTIONS
#VCC - 3.3V/ 5V
#GND - GND
#TRIG - 33 (ANY GPIO)
#ECHO - 32 (ANY GPIO)
#LCD  PIN CONNECTIONS
#SDA AND SCL - SDA AND SCL OF ESP32
#VCC - 5V
#GND - GND
#upload lcd library if you are using lcd sensor

from hcsr04 import HCSR04
from time import sleep

# ESP32
sensor = HCSR04(trigger_pin=33, echo_pin=32, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print("Distance: ", distance, "cm")
    sleep(3)
    lcd.putstr("Distance:")
    lcd.putstr(str(distance))
    lcd.putstr("cm")
    sleep(2)
    lcd.clear()
  



