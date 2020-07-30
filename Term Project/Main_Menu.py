#Main menu of the program
import os
from grove_library import arduinoDigitalRead, arduinoInit
from time import sleep
cls = lambda: os.system('cls')

#For manual testing
connection = arduinoInit('COM3')

cls()

#Main menu, infinite loop that stops once interrupted (When user presses button) (CTRL + C for computer)
def main_menu_idle():
    print("This is the main menu. Remaining Idle until needed.")
    time = 0
    while True:
        try:
            time += 1
            sleep(1)
        except KeyboardInterrupt:
            break
        

    return print("I've been idle for "+ str(time) +" seconds. What can I help you with?")
main_menu_idle()

#Import results from the What_Drink function
from What_Drink import drink
    
print("You want "+ str(drink))
print("Now serving " + str(drink))

#Import result from Flow_Sensor
from Flow_Sensor import result


print(str(round(result,2))+ "mL")
#Using outputs from previous two funtions (What_Drink and Flow_Sensor) and telling the user the nutritional value of what they drank.
def nutrition(drink,result):
    if drink == "Water":
        print("Despite having almost no nutritional value, water is important. Did you drink 8 cups today?")
        calcium = result * 0.03
        magnesium = result * 0.02
        sodium = result * 0.02
        print("All displayed information is in grams (g) " +"Calcium:" + str(round(calcium,2)), "Magnesium:" +str(round(magnesium,2)), "Sodium:"+str(round(sodium,2)))

    if drink == "Ice Tea":
        print("Good taste, but bad for health.")
        calories = result * 0.35
        sugar = result * 0.08
        sodium = result * 0.02
        potassium = result * 0.15
        caffeine = result * 0.00003
        print("All displayed information is in grams (g) " +"Calories:"+ str(round(calories,2)), "Suger:"+str(round(sugar,2)),"Sodium:"+ str(round(sodium,2)),"Potassium:"+ str(round(potassium,2)),"Caffeine:"+ str(round(caffeine,2)))
nutrition(drink,result)

#Imports an annoying ad. Intended to play only for users without 'Pro' version of the product.   
import ads_exe

sleep(3)