msg = str(input("Hello how are you doing? "))
print(msg)
FirstQ = str(input("What is your name "))
print("Your name is " , FirstQ , "Correct?")
while True:
    SecondQ = str(input("Reply with yes or no "))
    if SecondQ == ("Yes") or SecondQ == ("yes"):
        print("That is a pretty sweet name you have there.")
        break
    
    elif SecondQ == ("No") or SecondQ == ("no"):
        print("Why didn't you tell me your name?")
        break

    else:
        print("You didn't respond to my question")

print("Mind sharing me to your friend? I want to learn the names of others.")