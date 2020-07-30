##ENGI1020 Lab 6 Python Script##

##First we import libraries we might need##
from grove_library import *
import math
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import numpy as np


##Next we define functions we will call in the script##

## TODO Section 3.2 - Define function that modifies output based on input

def temp_to_light(temp):
    lightlevel = -16*temp + 480
    print("light level should be " + str(lightlevel))
    return lightlevel

##Now we have the script that will run##
def temp_average(analogList):
    sum_analogList = []
    for nums in analogList:
        sum_analogList.append(nums)
    tempavg = sum(sum_analogList) / len(analogList)
    print("The temperature average is "+ str(tempavg))
    return tempavg
# Call function to initialize the Arduino
connection = arduinoInit(0)

## TODO Section 3.3- Replace literal values with pin values of devices
analogPin = 0
digitalInPin = 7
digitalOutPint = 2

## TODO Section 3.3 - Initialize RGB LEDs or LED Bar

chainLEDInit(digitalOutPint, 2, connection)
barInit(digitalOutPint)

# Create empty list to collect analog readings

analogList = []


# Loop to collect readings
## TODO Section 3.1 - Modify WHILE loop to do the following
## - Append information from the analog sensor to the existing list
## - Wait 1 second
## until the button is pressed
while arduinoDigitalRead(7) != 1:
    analogList.append(round(tempGetCelsius(0),2))
    print("input taken")
    sleep(1)
    

# Debug information, prints info in analogList
for i in range(0, len(analogList)):
    print(analogList[i])

fakeList = [1, 2, 3, 4, 5]
fakeList[0]
len(fakeList)

tempavg = temp_average(analogList[:5])
lightlevel = temp_to_light(tempavg)


# TODO Section 3.4 - Modify below code to plot samples collected
plt.plot(analogList)
plt.xlabel('Time in seconds')
plt.ylabel('Temperature in Cesius')
plt.show()
