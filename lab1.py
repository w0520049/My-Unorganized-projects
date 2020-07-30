##ENGI1020 Lab 1 Python Script##

##First we import libraries we might need##
from grove_library import *
import math
from time import sleep


##Next we define functions we will call in the script##

# This function uses mathematical relationships to 'translate' hue to RGB
def lcdSetHue(hue):
    h = float(hue)
    s = float(1)
    v = float(0.5)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    lcdSetBackground(r, g, b)


##Now we have the script that will run##

# Call function to initialize the Arduino
connection = arduinoInit(0)

# TODO - Call function to initialize other components (ie. LCD screen, speaker)
# See Step 3.2 in Lab 1 Procedure

# TODO - Call function to get information from input
# See Step 3.2 in Lab 1 Procedure
lcdInit(connection)
arduinoAnalogRead(4)
lcdSetHue(tempGetCelsius(4))
# TODO - Implement mathematical relationship that maps input and output
# See Lab 1 Preparation and Step 3.1 in Lab 1 Procedure

# TODO - Call function to manipulate output
# See Step 3.2 in Lab 1 Procedure



