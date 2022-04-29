from measureInputs import measureInputsAndDriveValve
from driveValve import controlValve
from detectPlungerArrival import plungerDetector
from mqttManager import MQTTManager
from uuid import uuid4
import time
import threading
import RPi.GPIO as GPIO
import os
import yaml

MQTT_SENSOR_MEASUREMENT_TOPIC = 'RPi/Data-test'
MQTT_VALVE_STATE_TOPIC = 'RPi/ValveState-test'
MQTT_PLUNGER_ARRIVAL_TOPIC = 'RPi/PlungerArrivals-test'

measurmentPeriod = 0.2 #Seconds
valveOnTime = 5 #Seconds
valveOffTime = 30 #Seconds
noiseOnOffPct = 0.1 #%

rawCsMinusLn = 17000
rawFlowRateEndFlow = 7834
minOnTime = 3 #seconds
minOffTime = 15 #seconds
noisePct = 0. #Pct change of valve

pinPlungerArrival = 21
cvOpenPin = 25
cvClosePin = 23

#certFolder = '/home/pi/certificates/'

with open("./config.yaml", 'r') as stream:
    try:
        config_yaml=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print(f'Config Yaml: {config_yaml}')

#https://github.com/SmartDogHouse/SmartDogHouse-SurveillanceSystem/tree/cf14788c53f9c7a884ae9cc3e5f0839fdd18713c/src/main/python
mqttManager = MQTTManager(
	cert_path = config_yaml['system']['certificateFilePath'],#os.path.join(certFolder,'b7bea54d68aaa63204da17087aa3d7363d45f6dc76a29b0faf30dea3101daffc-certificate.pem.crt'),#'/home/pi/Desktop/RasberryPi-1.cert.pem',
        key_path =  config_yaml['system']['privateKeyPath'],#os.path.join(certFolder,'b7bea54d68aaa63204da17087aa3d7363d45f6dc76a29b0faf30dea3101daffc-private.pem.key'),#'/home/pi/Desktop/RasberryPi-1.private.key',
        root_path = config_yaml['system']['rootCaPath'],#os.path.join(certFolder,'AmazonRootCA1.pem',#'/home/pi/Desktop/root-CA.crt',	cert_path = '/home/pi/Desktop/RasberryPi-1.cert.pem',
	port = 8883,
	client_id = 'basicPubSub',
        server = 'a2upkalo7i6cik-ats.iot.us-east-1.amazonaws.com'
	)

try:
	mqttManager.connect()
except Exception as e:
	print('Cannot connect MQTT: ' + str(e))
	raise(e)

controlValve = controlValve(cvOpenPin,cvClosePin,valveOnTime,valveOffTime,mqttManager,MQTT_VALVE_STATE_TOPIC,noiseOnOffPct)

def publishSensorMeasurment():
	threading.Timer(measurmentPeriod, publishSensorMeasurment).start()
	mqttManager.send_msg(topic=MQTT_SENSOR_MEASUREMENT_TOPIC, msg=measureInputsAndDriveValve(controlValve, rawCsMinusLn, rawFlowRateEndFlow, minOnTime, minOffTime, noisePct))


##Start opening and closing the control valve


#controlValve = controlValve(cvOpenPin,cvClosePin,valveOnTime,valveOffTime,mqttManager,MQTT_VALVE_STATE_TOPIC,noiseOnOff)
#controlValve.openValveStartCycle()

#Start recording and uploading plunger arrivals
plgrDetector = plungerDetector(pinPlungerArrival,mqttManager,mqttTopic=MQTT_PLUNGER_ARRIVAL_TOPIC,threshold = 20000)
plgrDetector.beginDetectingPlungerArrivals() 
#threading.Thread(target=test).start()

#This function schedules itself
publishSensorMeasurment()

while True:
	#This exists so it can be force quit to stop sending measurments
	time.sleep(10)
