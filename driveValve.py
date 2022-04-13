from gpiozero import OutputDevice
import threading
from random import random

#MQTT_VALVE_STATE_TOPIC = 'RPi/ValveState'

class controlValve:
	def __init__(self, openPin,closePin,onTime,offTime,mqttManager,mqttTopic):
		self.openPin = OutputDevice(openPin)
		self.closePin = OutputDevice(closePin)
		self.onTime = onTime
		self.offTime = offTime
		self.mqttManager = mqttManager
		self.mqttTopic = mqttTopic

	def openValveStartCycle(self):
		threading.Timer(self.onTime, self.closeValve).start()
		self.closePin.off()
		self.openPin.on()
		self.mqttManager.send_msg(topic=self.mqttTopic, msg={"ValveOpen" : True})

	def closeValve(self):
		threading.Timer(self.offTime, self.openValveStartCycle).start()
		self.openPin.off()
		self.closePin.on()
		self.mqttManager.send_msg(topic=self.mqttTopic, msg={"ValveOpen" : False})

		
