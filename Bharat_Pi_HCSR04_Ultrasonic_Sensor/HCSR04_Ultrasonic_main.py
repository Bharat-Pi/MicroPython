/*************************************************************************
   PROJECT: Bharat Pi Ultrasonic sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing of ultrasonic sensor,
   which will measure the distance and
   prints the distance values in cm when you run the code.
   #upload lcd library from Bharapi_lcd_display folder if you are using lcd sensor with Ultrasonic

   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/
       
import machine
from hcsr04 import HCSR04
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from lcd_i2c import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

#initializing the I2C method for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  

#initializing the I2C method for ESP8266
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


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


