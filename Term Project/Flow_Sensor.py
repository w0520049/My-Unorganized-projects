#This is the program that will Initiate and Input the values from the Flow Sensor.
import os
from time import sleep
from grove_library import arduinoDigitalRead, arduinoInit
cls = lambda: os.system('cls')

#Uncomment below to test only Flow_Sensor
#connection = arduinoInit('COM3')

#Sensor operates like a lever, with it always being true or false.
#Takes in input from Flow Sensor and converts to mL (using what I know about how it orperates)
def convert_to_ml():
    print("Flow sensor online!")
    
    flowrate_mL = []
    time = 0
    while True:
        reading = float(arduinoDigitalRead(2))
        try:
            if reading > 0:
                flowrate_mL.append(reading*1000/60)
                time += 1
                print(flowrate_mL[-1] , time)
                sleep(1)
            elif reading <= 0:
                print(0,time)
                sleep(1)
            
        except KeyboardInterrupt:
            break
    cls()
    print("Flow sensor offline, here are the results.")
    liquid_amount = (float(sum(flowrate_mL)/len(flowrate_mL)))*float(time)
    return liquid_amount
result = convert_to_ml()
