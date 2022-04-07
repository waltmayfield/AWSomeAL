import detectPlungerArrival
from threading import Thread
import time
from RPi import GPIO

GPIO.add_event_detect(, GPIO.FALLING, callback=doorEvent, bouncetime=300)


Thread(target=detectPlungerArrival.detectPlungerArrival).start()

while True:
	time.sleep(10)

