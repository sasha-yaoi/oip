import RPi.GPIO as GPIO
import time as t
leds=[2,3,4,17,27,22,10,9]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)   
for a in range (3):
    for i in range (len(leds)):
        GPIO.output(leds[i],1)
        t.sleep(0.2)
        GPIO.output(leds[i],0)
GPIO.output(leds,0)
GPIO.cleanup()   


