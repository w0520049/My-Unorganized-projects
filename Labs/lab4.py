##ENGI1020 Lab 4 Python Script##

##First we import libraries we might need##
from grove_library import *
import math
from time import sleep


##Next we define functions we will call in the script##

# This function will convert input to output
def convertInputToOutput(input):
    '''
    Parameter input is your input value
    '''
    # TODO Section 3.1 - Implement mathematical expression from Design Part 1

# This function will get the avg of five samples from given port
def averageFiveSamples(pin):
    '''
    Parameter pin is the analog or digital port your device
	is plugged into
    '''
    # TODO Section 3.3 - Implement pseudocode from Design 2
	
# This function will modify the brightness of one LED
def chainLEDSetBrightness(index, brightness):
    '''
    Parameter index is which LED, 0 <= index < count
	Parameter brightness is setting, 0 <= brightness <= 1
    '''
    cVal = brightness * 255.0
    chainLEDSetColour(index, cVal, cVal, cVal)

##Now we have the script that will run##

# Call function to initialize the Arduino
connection = arduinoInit(0)
# TODO Section 3.4 - Initialize components that require it
chainLEDInit(2, 1, connection)

# Run system
# TODO Section 3.3 - Implement flow chart from Design Part 3
