#!/bin/bash

echo "Starting main program" > /tmp/AWSomeAL.out

#This is to help networking come up before running this program
sleep 25s

python3 /home/pi/AWSomeAL/main.py
# >> /tmp/AWSomeAL.out


