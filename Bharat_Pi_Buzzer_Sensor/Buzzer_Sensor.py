from machine import Pin
import time

BUZZER_PIN = 23  # GPIO pin connected to the buzzer

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
