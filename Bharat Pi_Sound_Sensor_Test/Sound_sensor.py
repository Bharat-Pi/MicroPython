#PIN CONNECTION
#AO - 12
#VCC - 3.3V
#GND - GND

from machine import ADC

# Define the analog pin connected to the sound sensor
sound_pin = 12

# Create an ADC object with the specified pin
adc = ADC(sound_pin)

while True:
  # Read the analog value from the sensor (0-1023)
  sound_val = adc.read()

  # Print the sound value (higher value indicates louder sound)
  print("Sound level:", sound_val)

  # You can add logic here to trigger actions based on sound level
  if sound_val > 120:
    print("Loud sound detected!")

  # Adjust delay time as needed
  time.sleep(3)

