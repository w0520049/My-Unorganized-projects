# This program will be used to calculate the volume and the area of a cylinder
# with the added benefits of the user being able to imput their required variables
# This program was made by Michael Laprise using past experience with coding a
# quadratic equation.

print("Welcome to the cylinder calculator. Please imput your known variables. ")
while True:
    print("""The mathematical equations for the volume of a cylinder is πr^2h
    and the equation for thee surface area is 2πr^2 + 2πrh. Pi is round to 3.1415
    in this program. """)
    #This is where the user inputs their values
    radius = float(input("Please input your known radius "))
    height = float(input("Please input your known height "))
    pi = 3.1415
    def volume_cylinder(radius,height,pi):
        volume = (pi * (radius**2) * height)
        return volume
        #Calculates volume
    
    def surface_area(radius,height,pi):
        area = ((2*pi*(radius**2)) + (2*pi*radius*height))
        return area
        #Calculates Area (total surface area)
    
    print("Volume is ",round(volume_cylinder(radius, height, pi), 2), "Surface area is " ,
     round(surface_area(radius, height, pi), 2))
     #Prints the answers
    question = str(input("Do you need help with another equation? "))
    if question == ("yes") or question == ("Yes") or question == ("YES"):
        print("Ok, here we go again. ")
    elif question == ("no") or question == ("No") or question == ("NO"):
        print("Hope I was helpful, see you again. ")
        break
    ###If user responds with yes, the code restarts from While true:
    # , if they respond no, the program ends
