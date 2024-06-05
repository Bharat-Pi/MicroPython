/*************************************************************************
   PROJECT: Bharat Pi Sound Sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing of sound sensor,
   which will detect the surrounding sound
   and gives the sound value as output when you run the code.
      #PIN CONNECTIONS
      #AO - 12
      #VCC - 3.3V
      #GND - GND
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/



from machine import ADC
import time

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
  if sound_val > 150:
    print("Loud sound detected!")

  # Adjust delay time as needed
  time.sleep(3)
