import random
import os
from time import sleep
cls = lambda: os.system('cls')
money = 100
sleep(2)
#Write your game of chance functions here
def game_of_heads_and_tails(money):
    while True:
        cls()
        heads_or_tails = random.randint(1,2)
        while True:
            heads_or_tails_guess = input("Heads or Tails? ")
            if heads_or_tails_guess == "heads" or heads_or_tails_guess == "Heads" or heads_or_tails_guess == "Head" or heads_or_tails_guess == "head":
                heads_or_tails_guess = 1
                break
            elif heads_or_tails_guess == "tails" or heads_or_tails_guess == "Tails" or heads_or_tails_guess == "Tail" or heads_or_tails_guess == "tail":
                heads_or_tails_guess = 2
                break
            else:
                print("You did not type the proper word.")
        
        if heads_or_tails == 1:
            print("It was Heads!")
        elif heads_or_tails == 2:
            print("It was Tails!")
        if heads_or_tails == heads_or_tails_guess:
            print("You guessed correctly. You win 2 dollars")
            money = money + 2
        else:
            print("You guessed incorrectly. You lose 1 dollar")
            money = money - 1

        print("Your balance is "+str(money))   
        yes_or_no = input("Do you want to flip the coin again? ")
        if yes_or_no == "yes" or yes_or_no == "Yes":
            print("Here we go again")
        elif yes_or_no == "no" or yes_or_no == "No":
            break
        else:
            print("You didnt say 'No', restarting game.")
    return money
    sleep(2)

money = game_of_heads_and_tails(money)

def game_of_die(money):
    while True:
        cls()
        dice_roll = random.randint(1,6)
        dice_guess = int(input("What side of 6 sided die do you think is facing up? "))
        print("The die landed with "+ str(dice_roll) + " facing up!")
        if dice_roll == dice_guess:
            print ("You guessed correctly. You win 5 dollars")
            money = money + 5
        elif dice_roll != dice_guess:
            print("You did not guess correclty. You lose 2 dollars")
            money = money - 2

        print("Your balance is "+str(money))  
        yes_or_no = input("Do you want to role the die again? ")
        if yes_or_no == "yes" or yes_or_no == "Yes":
            print("Here we go again")
        elif yes_or_no == "no" or yes_or_no == "No":
            break
        else: 
            print("You didnt say 'No', restarting game.")
    return money
    sleep(2)

money = game_of_die(money)
cls()
print("Thank you for playing.")