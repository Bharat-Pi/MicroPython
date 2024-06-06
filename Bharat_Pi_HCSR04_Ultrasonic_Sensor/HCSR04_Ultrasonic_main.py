/*************************************************************************
   PROJECT NAME:  Bharat Pi Ultrasonic sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of ultrasonic sensor,
   which will measure the distance and
   prints the distance values in cm when you run the code.
   #PIN CONNECTIONS:
   VCC   -   3.3V
   TRIG   -   33
   ECHO   -   32
   GND   -   GND

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of ultrasonic sensor sample script to read the data(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

 *************************************************************************/     
       
from machine import Pin, time_pulse_us
import time

# Define pins
TRIG_PIN = 33  # GPIO pin for the trigger
ECHO_PIN = 32  # GPIO pin for the echo

# Set up pins
TRIG = Pin(TRIG_PIN, Pin.OUT)
ECHO = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    # Send a 10µs pulse on the trigger pin
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    # Measure pulse duration on echo pin
    pulse_duration = time_pulse_us(ECHO, 1)
    
    # Calculate distance (divide by 58 to convert microseconds to centimeters)
    distance_cm = pulse_duration / 58.0  

    return distance_cm

try:
    while True:
        distance = measure_distance()
        print("Distance:", distance, "cm")
        time.sleep(1)

except KeyboardInterrupt:
    pass




