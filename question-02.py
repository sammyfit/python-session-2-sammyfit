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

num1 = ____  # Enter first number
num2 = ____  # Enter second number
operation = ____  # Enter '+', '-', '*', or '/'

if operation  ___ '+':
    print("Result:", num1 ___ num2)
elif operation == '-':
    ___("Result:", num1 - num2)
___ operation == '*':
    print("Result:", num1 * num2)
elif operation == '___' and num2 != 0:
    print("Result:", num1 / num2)
else:
    print("Invalid Operation or Division by Zero")
