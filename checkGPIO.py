import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BOARD)
##GPIO.setup(10,GPIO.OUT)
##GPIO.output(10,GPIO.HIGH)
##GPIO.cleanup()
import time

GPIO.setmode(GPIO.BOARD)

for i in ([12]):  # [5,7,11,12,14,16,18,22,13,15,19,21]
    print(i)
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.IN)
    time.sleep(0.2)

GPIO.cleanup()
# PI5=GPIO5
# PI7=GPIO7
# PI12=GPIO12
# PI3=GPIO13
# PI14=GPIO14
# PI5=GPIO15
# PI6=GPIO16
# PI8=GPIO18
# PI19=GPIO19
# P21=GPIO21
# PI22=GPIO22

