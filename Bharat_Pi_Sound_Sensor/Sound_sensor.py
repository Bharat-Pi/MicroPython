/*************************************************************************
   
   PROJECT NAME: Bharat Pi Sound Sensor Sample Code
   AUTHOR: Bharat Pi
   CREATED DATE: 25/03/2024
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
   VERSION: 0.1.1

   DESCRIPTION: This script will give you the sample testing of sound sensor,
   which will detect the surrounding sound
   and gives the sound value as output when you run the code.
   #PIN CONNECTIONS
   AO - 12
   VCC - 3.3V
   GND - GND

   REVISION HISTORY TABLE:
   ------------------------------------------
   Date      | Firmware Version | Comments
   ------------------------------------------
   25/03/2024 -    0.1.0       -    Initial release of sound sensor sample script to read the data(Used PyCraft IDE version - 1.1).
   06/06/2024 -    0.1.1       -    Added the altered code for Thonny ide(Used Thonny IDE version - 4.1.4).

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
