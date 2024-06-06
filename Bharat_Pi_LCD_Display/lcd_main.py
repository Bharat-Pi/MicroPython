/*************************************************************************
   PROJECT NAME: Bharat Pi LCD sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of LCD sensor,
   which will prints the message content on its display when you run the code.
    #PIN CONNECTION
    #GND - GND
    #VCC - 5V
    #SDA - SDA(ESP32)
    #SCL - SCL(ESP32)

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of lcd sensor sample script to print the data on display(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

 *************************************************************************/   

import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from lcd_i2c import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    lcd.putstr("This is BharatPi")
    sleep(3)
    lcd.clear()
    lcd.putstr("I2C LCD Tutorial")
    sleep(3)
    lcd.clear()
    lcd.putstr("Lets Count 0-10!")
    sleep(3)
    lcd.clear()
    for i in range(11):
        lcd.putstr(str(i))
        sleep(1)
        lcd.clear()
    lcd.putstr("Thank you")
    sleep(3)
    lcd.clear()


