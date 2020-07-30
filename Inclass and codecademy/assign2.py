#Started from scratch because it's how I do my work.
print("Welcome to the super awesome simple calculator for super simple equations performed in Python 3!")
print("Please tell me what you need to do.")
print("Press 1 for Addition", "Press 2 for Substractions","Click 3 for Multiplications")
print("Press 2 for Substractions")
print("Click 3 for Multiplications")
print("Punch 4 for Devision")
print("Enter 5 for Concatenation")
a = int(input("Enter your the program you want: "))
num1 = float(input("Var1: "))
num2 = float(input("Var2: "))
if a == 1:
    print(float(num1 + num2))
elif a == 2:
    print(float(num1 - num2))
elif a == 3:
    print(float(num1 * num2))
elif a == 4:
    if num2 == 0:
        print("ERROR")
    print(float(num1 / num2))
elif a == 5:
    if num1 % 1 ==0:
        num1 = int(num1)
    if num2 % 1 ==0:
        num2 = int(num2)
    print(str(num1)+ str(num2))
else:
    print("ERROR")
