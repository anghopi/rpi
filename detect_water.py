import RPi.GPIO as GPIO
import time
import datetime

gpio_buzzz=21
gpio_water=12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_water,GPIO.IN)
GPIO.setup(gpio_buzzz,GPIO.OUT)
try:
        while(True):

                water_true = GPIO.input(gpio_water)
                if water_true == GPIO.LOW:
                        print("water!!")
                        for i in range(1000):
                                GPIO.output(gpio_buzzz,GPIO.HIGH)
                                time.sleep(1e-9)
                                GPIO.output(gpio_buzzz,GPIO.LOW)
                                time.sleep(1e-9)
finally:
        GPIO.cleanup()




##        val=GPIO.input(gpio21)
##        if val==GPIO.HIGH:
##            print('\nHIGH at '+ str(datetime.datetime.now()))
##            GPIO.output(gpio12,GPIO.HIGH)
##        else:
##            print('\nLOW at '+ str(datetime.datetime.now()))
##            GPIO.output(gpio12,GPIO.LOW)