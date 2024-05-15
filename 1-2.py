import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.IN)

while True:
    a = GPIO.input(26)
    print(a)
    GPIO.output(21, a)