/*************************************************************************
   PROJECT: Bharat Pi Ultrasonic sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing of ultrasonic sensor,
   which will measure the distance and
   prints the distance values in cm when you run the code.
   #upload lcd library from Bharapi_lcd_display folder if you are using lcd sensor with Ultrasonic

   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
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




