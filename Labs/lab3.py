##ENGI1020 Lab 3 Python Script##

##First we import libraries we might need##
from grove_library import *
import math
from time import sleep

#Connect to the arduino
connection = arduinoInit(0)

#Gets c from sensor, then convert c to f
c = tempGetCelsius(1)
c = 29
def celsiusToFahrenheit(c):
    f = (c*(9/5))+32
    return f
f = celsiusToFahrenheit(c)

# Gather input from user
maxV = float(input('Maximum value in range to check: '))
minV = float(input('Minimum value in range to check: '))
loops = int(input('Number of iterations: '))
time = int(input('Seconds between loops: '))

#While true starts the loop
while True:

    #Checks if loops is not equal or less than 0
    if loops != 0 or loops > 0:

        #checks the value of f
        if f >= minV and f <= maxV:
            #print was for debugging aka checking if code worked until now
            print("It is hot")
            #arduinoDigitalWrite is the LED, 2 is the port, 1 and 0 are on and off
            arduinoDigitalWrite(2,1)
            #time is in seconds
            sleep(time)
            arduinoDigitalWrite(2,0)
            loops = loops - 1
            sleep(1)
    #These elif check to see if f is outside of the perameters
    #break is used to exit the while True loop
    elif f < minV:
        print("It is not hot enough")
        break
    elif f > maxV:
        print("It is too hot")
        break
    else:
        print("Loop has ended")
        break
