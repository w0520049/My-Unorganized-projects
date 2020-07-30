#Default program that was here at the start, might aswell keep it
print("This code prints a palindrome half/full pyramid of numbers")

#Take row numbers as input from user
#The assigment asked for 'n' to be assigned as the number of rows the user wants to print
n = int(input("How many rows do you want? "))

#Write the code to print full pyramid
#def to keep it clean
def palindrome_pyramid(n):
    
    #Gives i the perameters for future use. Think of i as a box where the pyramid
    #is found in. 
    for i in range(1, n+1):
        
        #Prints the nessesary spaces before the numbers
        for j in range(n - i):
            print(" ", end="")
            
        #Adds the first part of the triangle. From Left to Middle.
        for j in range(1, i):
            print(j,end="")

        #Finishes the triangle. From Middle to Right.
        for i in range(i, 0, -1):
            print(i, end = "")

        #End the code
        print("")

#Called the def here
palindrome_pyramid(n)

#Output of n=3 is:
#   1
#  121
# 12321