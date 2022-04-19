from gpiozero import OutputDevice
import threading
from random import random
from datetime import timezone
import datetime
import random

#MQTT_VALVE_STATE_TOPIC = 'RPi/ValveState'

class controlValve:
	def __init__(self, openPin,closePin,onTime,offTime,mqttManager,mqttTopic,noiseOnOff):
		self.openPin = OutputDevice(openPin)
		self.closePin = OutputDevice(closePin)
		self.onTime = onTime
		self.offTime = offTime
		self.mqttManager = mqttManager
		self.mqttTopic = mqttTopic
		self.noiseOnOff = noiseOnOff

	def openValveStartCycle(self):
		threading.Timer(self.onTime+self.noiseOnOff*(random.random()-0.5), self.closeValve).start()
		self.closePin.off()
		self.openPin.on()
		
		dt = datetime.datetime.now(timezone.utc)
		msg = {}
		msg['ValveOpen'] = True
		msg['ts']=str(dt.replace(tzinfo=None))
		
		self.mqttManager.send_msg(topic=self.mqttTopic, msg=msg)

	def closeValve(self):
		threading.Timer(self.offTime+self.noiseOnOff*(random.random()-0.5), self.openValveStartCycle).start()
		self.openPin.off()
		self.closePin.on()
		
		dt = datetime.datetime.now(timezone.utc)
		
		msg = {}
		msg['ValveOpen'] = False
		msg['ts']=str(dt.replace(tzinfo=None))

		self.mqttManager.send_msg(topic=self.mqttTopic, msg=msg)



		


		
