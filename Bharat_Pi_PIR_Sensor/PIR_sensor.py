/*************************************************************************
   PROJECT: Bharat Pi PIR Sensor Sample Code
   AUTHOR: Bharat Pi

   DESC: This script will give you the sample testing of pir sensor,
   which will detects the objects and 
   gives the alert message by turning on the led (motion detected) when detected.
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/
     
from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(23, Pin.OUT)
pir = Pin(18, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    led.value(1)
    sleep(10)
    led.value(0)
    print('Motion stopped!')
    motion = False

