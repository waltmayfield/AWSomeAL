sudo pip3 install awsiotsdk

#The function was being called before a DNS name could be resolved, so it may have come online too quickly. This sleep may resolve that.
sleep(10)

sudo python3 /home/pi/AWSomeAL/main.py
# & > /home/pi/Desktop/lastBootAWSomeAL.txt 2>&1
