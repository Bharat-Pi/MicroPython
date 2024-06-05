/*************************************************************************
   PROJECT: Bharat Pi Touch Sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing of touch sensor,
   which will detects/sense the touch and
   if touch detected prints the message (touch detected),
   if not then prints the message (no touch detected) when you run the code.
     #PIN CONNECTIONS
     #GND - GND
     #VCC - 3.3V
     #SIG - 32

   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/


from machine import Pin
import time

signal_pin = Pin(32, Pin.IN)

while True:
    state = signal_pin.value()
    print(state)
    if state == 1:
        print("Touch Detected")
    else:
          print("No Touch Detected")
    time.sleep(3)
