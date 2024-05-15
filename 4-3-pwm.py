import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
try:
    a=int(input("Введите коэффициент заполнения: "))
    p=GPIO.PWM(24,1000)
    p.start(a)
    input("Введите ключ для остановки")
    p.stop()
finally:
    GPIO.output(24,0)
    GPIO.cleanup()