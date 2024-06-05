/*************************************************************************
   PROJECT: Bharat Pi Blink LED Sample Code
   AUTHOR: Bharat Pi
   DESC: This script will give you the sample testing of blink led, which will do the LED light turn on and off for every one second when you run the code
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
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

