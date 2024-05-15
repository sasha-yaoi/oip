import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
while True:
    GPIO.output(27,1)
    t.sleep(1)
    GPIO.output(27,0)
    t .sleep(1)