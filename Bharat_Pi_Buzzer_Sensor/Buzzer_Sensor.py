/*************************************************************************
   PROJECT NAME: Bharat Pi Buzzer sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of buzzer sensor,
   which will give you the two different sounds/alerts in a loop when you run the script.
   #PIN CONNECTIONS
   S - 23
   GND - GND
   VCC - 3.3V
      
   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of buzzer sensor sample script to read the data(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

 *************************************************************************/

                                                          
from machine import Pin
import time

# GPIO pin connected to the buzzer
BUZZER_PIN = 23 

def setup():
    global buzzer
    
    # Initialize the buzzer pin
    buzzer = Pin(BUZZER_PIN, Pin.OUT)

def buzz(duration_ms):
    
    # Turn on the buzzer
    buzzer.on()
    # Wait for the specified duration
    time.sleep_ms(duration_ms)
    # Turn off the buzzer
    buzzer.off()

def loop():
    
    # First loop
    for i in range(100):
        # Make a sound
        buzzer.on()
        time.sleep_ms(1)  # Send high signal to buzzer
        buzzer.off()
        time.sleep_ms(1)  # Send low signal to buzzer
    time.sleep(1)
    
    for j in range(50):
        # Make another sound
        buzzer.on()
        time.sleep_ms(4)
        buzzer.off()
        time.sleep_ms(4)
    time.sleep(1)

# Initialize setup
setup()

# Main loop
while True:
    loop()




