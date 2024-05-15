import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time as t

measured_data=[]
all_time=[]
led=[2, 3, 4, 17, 27, 22, 10, 9]
dac=[8, 11, 7, 1, 0, 5, 12, 6]
bits=len(dac)
levels=2**bits
comp=14
troyka=13
maxvoltage=3.3 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
start_time=t.time()
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
    voltage=0
    while (voltage <= 2.65):
        value=adc()
        voltage = value/levels*maxvoltage
        print("Didigital = ",value,"Voltage = ", voltage)
        measured_data.append(voltage)
        all_time.append(t.time()-start_time)
    GPIO.output(troyka,0)
    while (voltage > 2.165625):
        value=adc()
        voltage = value/levels*maxvoltage
        print("Didigital = ",value,"Voltage = ", voltage)
        measured_data.append(voltage)
        all_time.append(t.time()-start_time)
    time_of_experiment=t.time()-start_time
    frequency=len(measured_data)/time_of_experiment
    quantization_step=3.3/256
    frequency_str=str(frequency)
    quantization_step_str=str(quantization_step)
    measured_data_str=[str(i) for i in measured_data]
    all_time_str=[str(i) for i in all_time]
    with open("data3.txt", "w") as outfile:
        outfile.write("\n".join(measured_data_str)) 
    with open("time3.txt", "w") as outfile:
        outfile.write("\n".join(all_time_str))                           
    with open("settings3.txt", "w") as outfile:
        outfile.write("Частота дискретизации: " + frequency_str + " Гц" + "\n")
        outfile.write("Шаг квантования: " + quantization_step_str + " В" + "\n")
    print ("Общая продолжительность эксперимента: ", time_of_experiment," c","\n")
    print ("Период одного измерения: ", 1/frequency, " с", "\n")   
    print ("Средняя частота дискретизации: ", frequency, " Гц", "\n")
    print ("Шаг квантования: ", quantization_step, " В", "\n")
    plt.plot(all_time,measured_data)
    plt.show()
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
