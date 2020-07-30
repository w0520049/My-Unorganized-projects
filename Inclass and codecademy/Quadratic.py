    #This is a program for solving quadratic equations ax**2 + bx + c
while True:
    print("Please entre your quadratic equation. ax**2 + bx + c")
    a = float(input("enter a "))
    b = float(input("enter b "))
    c = float(input("enter c "))
   
    d = (b**2)-(4*a*c)

    if d<0: print ("no solution")
    
    elif d == 0:
        x = (-b + (d**0.5)) / (2*a)
        print("There's only one solution possible" , x)
    
    else:
        x = (-b + (d**0.5)) / (2*a)
        y = (-b - (d**0.5)) / (2*a)
        print("There were two solutions to this problem" , x , y)

    ans = str(input("""Do you need help with another quadratic equation?
     Please reply only with yes or no. """))
    if ans == ("yes") or ans == ("Yes"):
        print("Ok here we go again")
    
    elif ans == ("no") or ans == ("No"):
        print("Ok hope to see you again :) ")
        break 
    