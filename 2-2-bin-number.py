import RPi.GPIO as GPIO
import time as t
dac=[6,12,5,0,1,7,11,8]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
n=8
number=[0,0,0,0,0,0,0,0]
GPIO.output(dac,number)
t.sleep(15)
GPIO.output(dac,0)
GPIO.cleanup() 

