/*************************************************************************
   PROJECT NAME: Bharat Pi Blink LED Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of blink led,
   which will do the LED light turn on and turn off for every one second when you run the code.

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of the sample script to test led blink(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

 *************************************************************************/
      
import machine
import time

# Define the pin number where the LED is connected
led_pin = 2

# Initialize the LED pin as an output
led = machine.Pin(led_pin, machine.Pin.OUT)

# Loop to blink the LED
while True:
    # Turn on the LED
    led.on()
    # Wait for 1 second
    time.sleep(1)
    # Turn off the LED
    led.off()
    # Wait for 1 second
    time.sleep(1)

