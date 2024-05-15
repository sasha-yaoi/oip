import RPi.GPIO as GPIO
import time as t
dac=[8,11,7,1,0,5,12,6]
leds=[2,3,4,17,27,22,10,9]
bits=len(dac)
levels=2**bits
comp=14
troyka=13
maxvoltage=3.3 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds, 1)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    vr=0
    tv=0
    for i in range(bits):
        pow2=2**(bits-i-1)
        tv=vr+pow2
        signal=decimal2binary(tv)
        GPIO.output(dac,signal)
        t.sleep(0.02)
        compv=GPIO.input(comp)
        if compv==0:
            vr=tv
    return vr
try:
    while True:
        value=adc()
        voltage = value/levels*maxvoltage
        print("Didigital = ",value,"Voltage = ", voltage)
        if value ==255:
            GPIO.output(leds,1)
        elif value>=32*7:
            GPIO.output(leds,[0,1,1,1,1,1,1,1])    
        elif value>=32*6:
            GPIO.output(leds,[0,0,1,1,1,1,1,1])  
        elif value>=32*5:
            GPIO.output(leds,[0,0,0,1,1,1,1,1])
        elif value>=32*4:
            GPIO.output(leds,[0,0,0,0,1,1,1,1]) 
        elif value>=32*3:
            GPIO.output(leds,[0,0,0,0,0,1,1,1])
        elif value>=32*2:
            GPIO.output(leds,[0,0,0,0,0,0,1,1])  
        elif value>=32*1:
            GPIO.output(leds,[0,0,0,0,0,0,0,1])     
        else: 
            GPIO.output(leds,0)                  
finally:
    GPIO.output(dac,0)
    GPIO.cleanup() 