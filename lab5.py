##ENGI1020 Lab 5 Python Script##

##First we import libraries we might need##
from grove_library import *
import math
from time import sleep
from random import randint


##Next we define functions we will call in the script##

# This function will run a competitive button-based game
    #TODO Section 3.1 - Implement stub function for speedWork() HERE
def speedWork(wait_Time, B1Pin, B2Pin):
    chainLEDSetColour(0,255,255,255)
    sleep(wait_Time)
    chainLEDSetColour(0, 255, 0, 0)
    time = 0
    while True:
        sleep(0.001)
        time = time + 1
        B1_input = arduinoDigitalRead(B1Pin)
        B2_input = arduinoDigitalRead(B2Pin)
        if B1_input == True and B2_input == False:
            chainLEDSetColour(0, 0, 255, 0)
            return "B1", time
        elif B2_input == True and B1_input == False:
            chainLEDSetColour(0, 0, 0, 255)
            return "B2", time
        elif B2_input == True and B1_input == True:
            cahinLEDSetColour(0, 255, 255, 255)
            return 0, time
        




    #stub function does not use input but provides output of expected type
        
def Play_again():
    answer = input("Do you want to play again: ")
    if answer == "Yes" or answer == "yes" or answer == "y" or answer == "Y":
        print("Restarting")
        w, t = speedWork(wait, button1Pin, button2Pin)
        if (w == 0):
                print(f'It is a tie in {t} milliseconds')
        else:
            print(f'Winner is Button {w} in {t} milliseconds')
    else:
        print("Ok, bye bye.")


# This function will run a co-operative rotary dial-based game
    #TODO Section 3.1 - Implement stub function for rightRotation() HERE
def Right_Rotation(target, R1Pin, R2Pin):
    #Stud function
    return 0, 0

##Now we have the script that will run##
## ONLY MODIFY THE PART BELOW WHERE IT SAYS
## "TODO Section 4..." ##

# Call function to initialize the Arduino
connection = arduinoInit(0)

# Rest of script depends on user selection
project = 0
while (project != 1 and project != 2):
    project = int(input('Enter 1 for Speed Work, 2 for Right Rotation: '))

# Speed Work
if project == 1:

    #Get RGB LED pin (must be in range) and initialize component
    ledPin = 0
    while not ((2 <= ledPin <= 8)):
        ledPin = int(input('Enter numeric value of RGB LED digital pin: '))

    chainLEDInit(ledPin, 1, connection)

    #Get button pins (must be in range and unique)
    button1Pin = 0
    button2Pin = 0
    while not ((2 <= button1Pin <= 8) and (2 <= button2Pin <= 8) and (button1Pin != button2Pin)):
        button1Pin = int(input('Enter numeric value of Button 1 digital pin: '))
        button2Pin = int(input('Enter numeric value of Button 2 digital pin: '))

        #Need to check they are unique from RGB LED too, otherwise reset to 0
        if (button1Pin == ledPin or button2Pin == ledPin):
            button1Pin = 0
            button2Pin = 0

    #User will choose testing or real game
    testing = int(input('Enter 1 to run tests, 0 to run real game: '))

    if (testing == 1):
        #Testing
        print('Running the function calls implemented in code for testing purposes')

        # TODO Section 4 - Implement function calls created in Preparation Part 4 and check outputs
    else:
        print('Running real game')

        #Generate wait before start time randomly
        wait = randint(1, 10)

        #Run game
        w, t = speedWork(wait, button1Pin, button2Pin)

        #Output results
        if (w == 0):
            print(f'It is a tie in {t} milliseconds')
        else:
            print(f'Winner is Button {w} in {t} milliseconds')
        Play_again()
            


# Right Rotation
elif project == 2:
    
    #Get LED Bar pin (must be in range) and initialize component
    barPin = 0
    while not ((2 <= barPin <= 8)):
        barPin = int(input('Enter numeric value of LED Bar digital pin: '))

    barInit(barPin)

    #Get rotary pins (must be in range and unique)
    rotary1Pin = -1
    rotary2Pin = -1
    while not ((0 <= rotary1Pin <= 3) and (0 <= rotary2Pin <= 3) and (rotary1Pin != rotary2Pin)):
        rotary1Pin = int(input('Enter numeric value of Rotary 1 analog pin: '))
        rotary2Pin = int(input('Enter numeric value of Rotary 2 analog pin: '))

    #User will choose testing or real game
    testing = int(input('Enter 1 to run tests, 0 to run real game: '))

    if (testing == 1):
        #Testing
        print('Running the function calls implemented in code for testing purposes')

        # TODO Section 4 - Implement function calls created in Preparation Part 4 and check outputs
    else:
        print('Running real game')

        #Generate rotary sum randomly
        targetVal = randint(0, 2046)

        #Run game
        r1Val, r2Val = rightRotation(targetVal, rotary1Pin, rotary2Pin)

        #Output results
        print(f'{r1Val} + {r2Val} = {targetVal}, hooray!!')


