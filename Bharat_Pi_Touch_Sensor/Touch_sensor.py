#PIN CONNECTIONS
#GND - GND
#VCC - 3.3V
#SIG - 32

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
