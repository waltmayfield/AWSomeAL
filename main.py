#!/usr/bin/env python
from measureInputs import measureInputs
from driveValve import controlValve
from mqttManager import MQTTManager
from uuid import uuid4
import time
import threading
import os

MQTT_SENSOR_MEASUREMENT_TOPIC = 'RPi/Test'
MQTT_VALVE_STATE_TOPIC = 'RPi/Test'

measurmentPeriod = 0.2 
valveOnTime = 2
valveOffTime = 45

certFolder = '/home/pi/certificates/'
#https://github.com/SmartDogHouse/SmartDogHouse-SurveillanceSystem/tree/cf14788c53f9c7a884ae9cc3e5f0839fdd18713c/src/main/python
mqttManager = MQTTManager(
	cert_path = os.path.join(certFolder,'b7bea54d68aaa63204da17087aa3d7363d45f6dc76a29b0faf30dea3101daffc-certificate.pem.crt'),#'/home/pi/Desktop/RasberryPi-1.cert.pem',
	key_path = os.path.join(certFolder,'b7bea54d68aaa63204da17087aa3d7363d45f6dc76a29b0faf30dea3101daffc-private.pem.key'),#'/home/pi/Desktop/RasberryPi-1.private.key',
	root_path = os.path.join(certFolder,'AmazonRootCA1.pem'),#'/home/pi/Desktop/root-CA.crt',
	port = 8883,
	client_id = 'basicPubSub',
        server = 'a2upkalo7i6cik-ats.iot.us-east-1.amazonaws.com'
	)

try:
    mqttManager.connect()
except Exception as e:
    print('Cannot connect MQTT: ' + str(e))


def publishSensorMeasurment():
	threading.Timer(measurmentPeriod, publishSensorMeasurment).start()
	mqttManager.send_msg(topic=MQTT_SENSOR_MEASUREMENT_TOPIC, msg=measureInputs())


controlValve = controlValve(24,23,valveOnTime,valveOffTime,mqttManager,MQTT_VALVE_STATE_TOPIC)
controlValve.openValveStartCycle()

#This function schedules itself
publishSensorMeasurment()


while True:
	#This exists so it can be force quit to stop sending measurments
	time.sleep(10)
