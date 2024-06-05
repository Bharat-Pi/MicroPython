/*************************************************************************
   PROJECT: Bharat Pi Accelerometer Sample Code
   AUTHOR: Bharat Pi
   DESC: This script will give you the sample testing of accelerometer sensor
 
   COPYRIGHT: BharatPi @MIT license for usage on Bharat Pi boards
 *************************************************************************/
                                   
from machine import Pin, SoftI2C
import time

# MPU6050 Register Addresses
MPU6050_ADDR = 0x68
MPU6050_ACCEL_XOUT_H = 0x3B
MPU6050_PWR_MGMT_1 = 0x6B

# Initialize I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# MPU6050 initialization
i2c.writeto_mem(MPU6050_ADDR, MPU6050_PWR_MGMT_1, bytearray([0]))

def read_acceleration():
  # Read raw acceleration values
  data = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 6)
   
  # Convert raw data to acceleration values
  accel_x = (data[0] << 8 | data[1]) / 16384.0
  accel_y = (data[2] << 8 | data[3]) / 16384.0
  accel_z = (data[4] << 8 | data[5]) / 16384.0
   
  return accel_x, accel_y, accel_z

# Main loop
while True:
  try:
    accel_x, accel_y, accel_z = read_acceleration()
    print("Acceleration (m/s^2):")
    print("X:", accel_x)
    print("Y:", accel_y)
    print("Z:", accel_z)
    
  except OSError as e:
    print("Error reading from MPU6050:", e)
  time.sleep(1)
