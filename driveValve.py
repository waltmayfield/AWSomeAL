from gpiozero import OutputDevice
import threading
from random import random
from datetime import timezone
import datetime
import random
from time import sleep

#MQTT_VALVE_STATE_TOPIC = 'RPi/ValveState'

class controlValve:
	def __init__(self, openPin,closePin,onTime,offTime,mqttManager,mqttTopic,noiseOnOffPct=0.):
		self.openPin = OutputDevice(openPin)
		self.closePin = OutputDevice(closePin)
		self.onTime = onTime
		self.offTime = offTime
		self.mqttManager = mqttManager
		self.mqttTopic = mqttTopic
		self.noiseOnOffPct = noiseOnOffPct
		
		#Initilize these both at the initilization time
		#self.lastValveClose = self.currentTime()
		#self.lastValveOpen = self.currentTime()
		self.lastValveStateChange = self.currentTime()
			
		#Close valve when initiate
		self.closeValve()
		self.valveOpen = False

	def currentTime(self):
		dt = datetime.datetime.now(timezone.utc)
		return dt.replace(tzinfo=None)		
		
	def openValve(self):
		#First chage valve state to prevent multiple open valve events
		self.valveOpen = True
		self.lastValveStateChange = self.currentTime() #This will be over-written later
		
		#Inject some noise into the control policy, based on the current time at valve state.
		sleep(random.random()*self.noiseOnOffPct*self.currentTimeSinceStateChange())
		
		self.closePin.off()
		self.openPin.on()
		currentTime = self.currentTime()
		self.lastValveStateChange = currentTime
	
		msg = {}
		msg['ValveOpen'] = self.valveOpen
		msg['ts']=str(currentTime)
		
		self.mqttManager.send_msg(topic=self.mqttTopic, msg=msg)

	def closeValve(self):
		#First change the valve state to prevent multile close valve eventss
		self.valveOpen = False
		self.lastValveStateChange = self.currentTime() #This will be over-written later
	
		#Inject some noise into the system		
		sleep(random.random()*self.noiseOnOffPct*self.currentTimeSinceStateChange())
		
		self.openPin.off()
		self.closePin.on()
		currentTime = self.currentTime()
		self.lastValveStatechange = currentTime
		
		msg = {}
		msg['ValveOpen'] = self.valveOpen
		msg['ts']=str(currentTime)

		self.mqttManager.send_msg(topic=self.mqttTopic, msg=msg)

#	def currentOnTime(self):
#		dt = datetime.datetime.now(timezone.utc).replace(tzinfo=None)
#		return (dt-self.lastValveStateChange).total_seconds()
	
#	def currentOffTime(self):
#		dt = datetime.datetime.now(timezone.utc).replace(tzinfo=None)
#		return (dt-self.lastValveStateChange).total_seconds()
	
	def currentTimeSinceStateChange(self):
		dt = datetime.datetime.now(timezone.utc).replace(tzinfo=None)
		return (dt-self.lastValveStateChange).total_seconds()
	
		


		
