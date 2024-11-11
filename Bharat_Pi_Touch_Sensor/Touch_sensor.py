/*************************************************************************
   
   PROJECT NAME: Bharat Pi Touch Sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of touch sensor,
   which will detects/sense the touch and
   if touch detected prints the message (touch detected),
   if not then prints the message (no touch detected) when you run the code.
   #PIN CONNECTIONS
   GND - GND
   VCC - 3.3V
   SIG - 32

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of touch sensor sample script to read the data(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

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
