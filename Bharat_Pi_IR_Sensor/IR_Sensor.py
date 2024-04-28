from machine import Pin
import time

SENSOR_PIN = 23  # GPIO pin connected to the IR sensor

def setup():
    global ir_sensor
    # Initialize the IR sensor pin
    ir_sensor = Pin(SENSOR_PIN, Pin.IN)

def loop():
    # Read the state of the IR sensor
    sensor_state = ir_sensor.value()

    # Check if the sensor state has changed
    if sensor_state == 1:
        print("Obstacle detected")
    else:
        print("Obstacle cleared")

    # Delay for a short period before reading again
    time.sleep(3)

# Initialize the setup
setup()

while True:
    loop()



