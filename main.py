from measureInputs import measureInputs
from driveValve import controlValve
from detectPlungerArrival import plungerDetector
from mqttManager import MQTTManager
from uuid import uuid4
import time
import threading
import RPi.GPIO as GPIO
import os

MQTT_SENSOR_MEASUREMENT_TOPIC = 'RPi/Test'#'RPi/Data'
MQTT_VALVE_STATE_TOPIC = 'RPi/Test'#'RPi/ValveState'
MQTT_PLUNGER_ARRIVAL_TOPIC = 'RPi/Test'#'RPi/PlungerArrivals'

measurmentPeriod = 0.2 
valveOnTime = 5
valveOffTime = 30

pinPlungerArrival = 21
cvOpenPin = 25
cvClosePin = 23

certFolder = '/home/pi/certificates/'
#https://github.com/SmartDogHouse/SmartDogHouse-SurveillanceSystem/tree/cf14788c53f9c7a884ae9cc3e5f0839fdd18713c/src/main/python
mqttManager = MQTTManager(
	cert_path = os.path.join(certFolder,'b7bea54d68aaa63204da17087aa3d7363d45f6dc76a29b0faf30dea3101daffc-certificate.pem.crt'),#'/home/pi/Desktop/RasberryPi-1.cert.pem',
        key_path = os.path.join(certFolder,'b7bea54d68aaa63204da17087aa3d7363d45f6dc76a29b0faf30dea3101daffc-private.pem.key'),#'/home/pi/Desktop/RasberryPi-1.private.key',
        root_path = os.path.join(certFolder,'AmazonRootCA1.pem'),#'/home/pi/Desktop/root-CA.crt',	cert_path = '/home/pi/Desktop/RasberryPi-1.cert.pem',
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
controlValve = controlValve(cvOpenPin,cvClosePin,valveOnTime,valveOffTime,mqttManager,MQTT_VALVE_STATE_TOPIC)
controlValve.openValveStartCycle()

#Start recording and uploading plunger arrivals
plgrDetector = plungerDetector(pinPlungerArrival,mqttManager,mqttTopic=MQTT_PLUNGER_ARRIVAL_TOPIC,threshold = 20000)
plgrDetector.beginDetectingPlungerArrivals() 
#threading.Thread(target=test).start()

#This function schedules itself
publishSensorMeasurment()

while True:
	#This exists so it can be force quit to stop sending measurments
	time.sleep(10)
