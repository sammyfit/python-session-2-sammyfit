"""
Program: Simple Calculator using if else statement and countinue as per the use choice

Description:
------------
This program performs basic arithmetic operations based on the user's input.
It accepts two numbers and an operation choice from the user.
The supported operations are:
    +  --> Addition
    -  --> Subtraction
    *  --> Multiplication
    /  --> Division (only if the second number is not zero)

After each calculation, the program asks the user if they want to continue.
If the user enters 'yes', it repeats the calculation process.
If the user enters 'no', the program quits with a goodbye message.
"""

while True:
    # Get user input and convert to integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Choose operation
    operation = input("Enter operation (+, -, *, /): ")

    # Perform operation using if-elif-else
    if operation == '+':
        result = num1 + num2
        print("Result:", result)
    elif operation == '-':
        result = num1 - num2
        print("Result:", result)
    elif operation == '*':
        result = num1 * num2
        print("Result:", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation choice.")

    # Ask user whether to continue
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break
