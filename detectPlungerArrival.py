from datetime import datetime
from datetime import timezone
import RPi.GPIO as GPIO

class plungerDetector:
	def __init__(self,pinPlungerArrival, mqttManager, threshold = 20000, topic = 'RPi/PlungerArrivals'):
		self.pinPlungerArrival = pinPlungerArrival
		self.mqttManager = mqttManager
		self.threshold = threshold
		self.topic = topic
	
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pinPlungerArrival, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def pinLowTime(self,pin):
	        startTime = datetime.now()
	        while GPIO.input(pin) == 0: pass
	        return (datetime.now()-startTime).microseconds

	
		
	def detectPlungerArrival(self,channel):
		deltat = self.pinLowTime(channel)	
		if deltat > self.threshold: 
			print(f'{datetime.now()}: Plunger pin low for {deltat} microseconds')
			msg = {'timeSpanMicroS':deltat}
			msg['ts']=str(datetime.now(timezone.utc).replace(tzinfo=None))
			self.mqttManager.send_msg(topic=self.topic, msg=msg)
			
		return deltat > self.threshold
	
	def beginDetectingPlungerArrivals(self):
		GPIO.add_event_detect(self.pinPlungerArrival, GPIO.FALLING, callback=self.detectPlungerArrival)#, bouncetime=10)	


if __name__ == '__main__':
	pinPlungerArrival = 21
	
	plgrDetector = plungerDetector(pinPlungerArrival,'')
	
	plgrDetector.beginDetectingPlungerArrivals()
	
	import time
	while True:
		time.sleep(10)
