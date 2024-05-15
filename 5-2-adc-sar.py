import RPi.GPIO as GPIO
import time as t
dac=[8,11,7,1,0,5,12,6]
bits=len(dac)
levels=2**bits
comp=14
troyka=13
maxvoltage=3.3 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    vr=0
    tv=0
    for i in range(bits):
        pow2=2**(bits-i-1)
        tv=vr+pow2
        signal=decimal2binary(tv)
        GPIO.output(dac, signal)
        t.sleep(0.005)
        compv=GPIO.input(comp)
        if compv==0:
            vr=tv
    return vr
try:
    while True:
        value=adc()
        voltage = value/levels*maxvoltage
        print("Didigital = ",value,"Voltage = ", voltage)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup() 