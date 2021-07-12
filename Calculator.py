#simple calculator

#addition
def add(x, y):
    return x + y
#subtraction
def subtract(x, y):
    return x - y
#multiplication
def multiply(x, y):
    return x * y
#division
def divide(x, y):
    return x / y
# random number
import random

def calculate():
    #operation selection.
    OptionList = ["1. Addition", "2. Subtract", "3. Multiply", "4. Division", "5. Generate random number"]
    print("\nPlease type in the math operation you would like to complete:\n")
    for x in OptionList:
        print(x, "\n")

    
    user_choice = input("Enter choice: ")    
    if user_choice == '1': 
        print("\nYou have chosen to perform addition \n")
    elif user_choice == '2':
        print("\nYou have chosen to perform subtraction \n")
    elif user_choice == '3':
        print("\nYou have chosen to perform multiplication \n")
    elif user_choice == '4':
        print("\nYou have chosen to perform division \n")
    elif user_choice == '5':
        print("\nYou have chosen to generate a random number \n")

    if user_choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter your first number: "))
        except Valu4eError:
             print("\nInvalid")
             again()
        try:
            num2 = int(input("\nEnter your second number: "))
        except ValueError:
            print("\nInvalid")
            again()
        
    if user_choice == '1':
        print("\nThe answer is: ", num1, "+", num2, "=", add(num1, num2), "\n")
    elif user_choice == '2':
        print("\nThe answer is: ", num1, "-", num2, "=", subtract(num1, num2), "\n")
    elif user_choice == '3':
        print("\nThe answer is: ", num1, "*", num2, "=", multiply(num1, num2), "\n")
    elif user_choice == '4':
        print("\nThe answer is: ", num1, "/", num2, "=", divide(num1, num2), "\n")    
    elif user_choice == '5':
        print("Your random number ranging from 1-100000 is: {}" .format(random.randint(1, 100000)), "\n")
    else: 
        print("Invalid Input \n")  
    again()
    
def again():
    calc_again = input ("Do you want to calculate again?\n(Type Y for YES or N for No:) ")
    
    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print("\nThank you, see you again")
        exit()
    else:
        again()
        
calculate()