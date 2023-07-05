import RPi.GPIO as GPIO
import datetime

channel = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

while (True):
    val = GPIO.input(channel)
    if val == GPIO.HIGH:
        print('\nHIGH at ' + str(datetime.datetime.now()))
    else:
        print('\nLOW at ' + str(datetime.datetime.now()))

GPIO.cleanup()
import RPi.GPIO as GPIO
import time

channel = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.OUT)
while (True):
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(0.0000074)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.0000074)

GPIO.cleanup()

#swave.py:
#import RPi.GPIO as GPIO
#import time
#
#channel = 12
#
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(channel, GPIO.OUT)
#while (True):
#    GPIO.output(channel, GPIO.HIGH)
#    time.sleep(0.0000074)
#    GPIO.output(channel, GPIO.LOW)
#    time.sleep(0.0000074)
#
#GPIO.cleanup()
