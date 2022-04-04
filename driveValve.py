from gpiozero import OutputDevice
import threading
from random import random
from datetime import timezone
import datetime

MQTT_VALVE_STATE_TOPIC = 'RPi/ValveState'

class controlValve:
	def __init__(self, openPin,closePin,onTime,offTime,mqttManager):
		self.openPin = OutputDevice(openPin)
		self.closePin = OutputDevice(closePin)
		self.onTime = onTime
		self.offTime = offTime
		self.mqttManager = mqttManager

	def openValveStartCycle(self):
		threading.Timer(self.onTime, self.closeValve).start()
		self.closePin.off()
		self.openPin.on()
		
		dt = datetime.datetime.now(timezone.utc)
		msg = {}
		msg['ValveOpen'] = True
		msg['ts']=str(dt.replace(tzinfo=None))
		
		self.mqttManager.send_msg(topic=MQTT_VALVE_STATE_TOPIC, msg=msg)

	def closeValve(self):
		threading.Timer(self.offTime, self.openValveStartCycle).start()
		self.openPin.off()
		self.closePin.on()
		
		dt = datetime.datetime.now(timezone.utc)
		
		msg = {}
		msg['ValveOpen'] = False
		msg['ts']=str(dt.replace(tzinfo=None))

		self.mqttManager.send_msg(topic=MQTT_VALVE_STATE_TOPIC, msg=msg)



		


		
