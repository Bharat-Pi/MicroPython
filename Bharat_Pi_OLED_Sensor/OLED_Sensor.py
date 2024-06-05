/*************************************************************************
   PROJECT: Bharat Pi OLED sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing f OLED sensor,
   which will prints the required message content on its display when you run the code.
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/


from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello ', 0, 0)
oled.text('welcomem to' , 0, 10)
oled.text('Bharat Pi ', 0, 20)
        
oled.show()
