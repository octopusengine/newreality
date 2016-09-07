#!/usr/bin/python

import smbus, time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x33      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#print "test i2c"
#test blink
for b in range(3):
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("L"))
	time.sleep(0.2)
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("H"))
	time.sleep(0.2)
	print ".",

#print ">> num"
#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("N"))
#print int(bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1))
#print bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
  
   
def getLabData(): 
   bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("H"))
   time.sleep(0.05)		
   #print bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
   data=bus.read_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0)
   bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, ord("L"))
   time.sleep(0.01)
   #print b,str(data) 
   return data
  
   

#Write a single register
#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
#ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
#bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
