
#Displays and asks the user what drink they want
drinks = ['Water','Ice Tea']
def what_drink(drinks):
    options = []
    for drink in drinks:
        options.append(drink)
    while True:
        user_input = str(input("I have "+ str(options) + " in stock, what can I get you: "))
        
        if user_input in drinks:
            break
        else:
            print("I'm sorry, I don't have that. Did you mistype the word?")
    return user_input

drink = what_drink(drinks)