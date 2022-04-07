# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import time
import json
from datetime import timezone
import datetime

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chanTbg = AnalogIn(mcp, MCP.P0)
chanCsg = AnalogIn(mcp, MCP.P1)
chanGas = AnalogIn(mcp, MCP.P2)
chanPA  = AnalogIn(mcp, MCP.P7) #Plunger Arrival Sensor

#dChannels = {'valTbg':chanTbg,'valCsg':chanCsg,'valGas':chanGas, 'valPA':chanPA}
dChannels = {'valTbg':chanTbg,'valCsg':chanCsg,'valGas':chanGas}

#print('Raw ADC Value: ', chanTbg.value)
#print('ADC Voltage: ' + str(chanTbg.voltage) + 'V')

def remap_range(value, left_min, left_max, right_min, right_max):
	# this remaps a value from original (left) range to new (right) range
	# Figure out how 'wide' each range is
	left_span = left_max - left_min
	right_span = right_max - right_min

	# Convert the left range into a 0-1 range (int)
	valueScaled = int(value - left_min) / int(left_span)

	# Convert the 0-1 range into a value in the right range.
	return int(right_min + (valueScaled * right_span))


def measureInputs():
	measurements = {key:value.value for key, value in dChannels.items()}
	measurements['ts']=str(datetime.datetime.now(timezone.utc).replace(tzinfo=None))
	#return json.dumps(measurments)
	return measurements

if __name__ == '__main__':
	while True:
		# read the analog pin
		#print(f'Tubing value: {chanTbg.value}')
		#print(f'Casing value: {chanCsg.value}')
		print(measureInputs())	
		
		time.sleep(1)
	
	
#
# SPDX-License-Identifier: MIT
