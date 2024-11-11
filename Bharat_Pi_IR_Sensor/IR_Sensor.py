/*************************************************************************
   PROJECT NAME: Bharat Pi IR sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of IR sensor,
   which will do the LED light turn on when any Obstacle detected near the sensor 
   and turn off the led when Obstacle cleared 
   and it will give the respective message for every three second when you run the code.
   #PIN CONNECTIONS:
   OUT   -   23
   GND   -   GND
   VCC   -   3.3V

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of IR sensor sample script to read the data(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

 *************************************************************************/


from machine import Pin
import time

# GPIO pin connected to the IR sensor
SENSOR_PIN = 23 

def setup():
    global ir_sensor
    # Initialize the IR sensor pin
    ir_sensor = Pin(SENSOR_PIN, Pin.IN)

def loop():
    
    # Read the state of the IR sensor
    sensor_state = ir_sensor.value()

    # Check if the sensor state has changed
    if sensor_state == 0:
        print("Obstacle detected")
    else:
        print("Obstacle cleared")

    # Delay for a short period before reading again
    time.sleep(3)

# Initialize the setup
setup()

while True:
    loop()


