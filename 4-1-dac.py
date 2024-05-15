import RPi.GPIO as GPIO
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        a=input()
        if a=="q":
            break
        if a.isdigit() is False:
            print("You have enter not a number")
        elif int(a)>256:
            print("The number is too big")
        else:
            GPIO.output(dac,decimal2binary(int(a)))
            print ((3.3/256)*int(a),"В")  
finally:
    GPIO.output(dac,0)
    GPIO.cleanup() 
