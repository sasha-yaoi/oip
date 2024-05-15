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
def adc(value):
    signal=decimal2binary(value)
    GPIO.output(dac,signal)
    return signal
try:
    while True:
        for value in range(256):
            signal=adc(value)
            t.sleep(0.001)
            voltage=value/levels * maxvoltage
            compv = GPIO.input(comp)
            if compv==1:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value,signal,voltage))
                break
finally:
    GPIO.output(dac,0)
    GPIO.cleanup() 