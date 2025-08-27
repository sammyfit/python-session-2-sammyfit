"""
Program: Simple Calculator using If-Elif-Else Statements

Description:
------------
This program performs basic arithmetic operations based on the user's input.
It accepts two numbers and an operation choice from the user.
The supported operations are:
    +  --> Addition
    -  --> Subtraction
    *  --> Multiplication
    /  --> Division (only if the second number is not zero)

get user user input using input() function and covert that numbers into integers

"""

num1 = int(input("First Number: "))  # Enter first number
num2 = int(input("Second Number: "))  # Enter second number
operation = input("Choose Operator -> Enter '+', '-', '*', or '/'")  # Enter '+', '-', '*', or '/'

if operation  == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/' and num2 != 0:
    print("Result:", num1 / num2)
else:
    print("Invalid Operation or Division by Zero")
