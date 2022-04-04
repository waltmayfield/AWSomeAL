from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from measureInputs import measureInputs
from mqttManager import MQTTManager
from uuid import uuid4
import time

#MQTT_SENSOR_MEASUREMENT_TOPIC = 'RPi/Data'
MQTT_SENSOR_MEASUREMENT_TOPIC = 'sdk/test/Python'

#https://github.com/SmartDogHouse/SmartDogHouse-SurveillanceSystem/tree/cf14788c53f9c7a884ae9cc3e5f0839fdd18713c/src/main/python
#mqttManager = MQTTManager(
#	cert_path = '/home/pi/Desktop/RasberryPi-1.cert.pem',
#	key_path = '/home/pi/Desktop/RasberryPi-1.private.key',
#	root_path = '/home/pi/Desktop/root-CA.crt',
#	port = None,
#	client_id = 'RaspberryPi-mqtt-1-' + str(uuid4()),
#        server = 'a2upkalo7i6cik-ats.iot.us-east-1.amazonaws.com'
#	)

clientId = 'basicPubSub'
host = 'a2upkalo7i6cik-ats.iot.us-east-1.amazonaws.com'
port = 8883 #This is the default port
rootCAPath = '/home/pi/Desktop/root-CA.crt'
privateKeyPath = '/home/pi/Desktop/RasberryPi-1.private.key'
certificatePath = '/home/pi/Desktop/RasberryPi-1.cert.pem'

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

print(f'\n\n\n clientId:{clientId}, {host}, {port}, {rootCAPath}, {privateKeyPath}, {certificatePath} \n\n\n ')

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

#mqttManager.connect()

#try:
#    mqttManager.connect()
#except Exception as e:
#    print('Cannot connect MQTT: ' + str(e))

while True:
	msg = measureInputs()
	print(f'MQTT message: {msg}')
	
	#mqttManager.send_msg(topic=MQTT_SENSOR_MEASUREMENT_TOPIC, msg=msg)

	myAWSIoTMQTTClient.publish(MQTT_SENSOR_MEASUREMENT_TOPIC, msg, 1)
	time.sleep(1)
