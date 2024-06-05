/*************************************************************************
   PROJECT: Bharat Pi IR sensor Sample Code
   AUTHOR: Bharat Pi
   DESC: This script will give you the sample testing of IR sensor, which will do the LED light turn on when any Obstacle detected near the sensor and turn off the led when Obstacle cleared and it will give the respective message for every three second when you run the code
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
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


