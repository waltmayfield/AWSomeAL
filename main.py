from measureInputs import measureInputs
from driveValve import controlValve
from detectPlungerArrival import plungerDetector
from mqttManager import MQTTManager
from uuid import uuid4
import time
import threading
import RPi.GPIO as GPIO

MQTT_SENSOR_MEASUREMENT_TOPIC = 'RPi/Data'

measurmentPeriod = 0.2 
valveOnTime = 10
valveOffTime = 45

pinPlungerArrival = 21
cvOpenPin = 25
cvClosePin = 23

#https://github.com/SmartDogHouse/SmartDogHouse-SurveillanceSystem/tree/cf14788c53f9c7a884ae9cc3e5f0839fdd18713c/src/main/python
mqttManager = MQTTManager(
	cert_path = '/home/pi/Desktop/RasberryPi-1.cert.pem',
	key_path = '/home/pi/Desktop/RasberryPi-1.private.key',
	root_path = '/home/pi/Desktop/root-CA.crt',
	port = 8883,
	client_id = 'basicPubSub',
        server = 'a2upkalo7i6cik-ats.iot.us-east-1.amazonaws.com'
	)

try:
	mqttManager.connect()
except Exception as e:
	print('Cannot connect MQTT: ' + str(e))
	raise(e)

def publishSensorMeasurment():
	threading.Timer(measurmentPeriod, publishSensorMeasurment).start()
	mqttManager.send_msg(topic=MQTT_SENSOR_MEASUREMENT_TOPIC, msg=measureInputs())

#Start opening and closing the control valve
controlValve = controlValve(cvOpenPin,cvClosePin,valveOnTime,valveOffTime,mqttManager)
controlValve.openValveStartCycle()

#Start recording and uploading plunger arrivals
plgrDetector = plungerDetector(pinPlungerArrival,mqttManager,threshold = 20000)
plgrDetector.beginDetectingPlungerArrivals()
#threading.Thread(target=test).start()

#This function schedules itself
publishSensorMeasurment()

while True:
	#This exists so it can be force quit to stop sending measurments
	time.sleep(10)
