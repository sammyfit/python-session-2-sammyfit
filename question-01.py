# Find the largest among three numbers , get input from user using input() function
num1 = 85   # Enter first number
num2 = 96   # Enter second number
num3 = 48   # Enter third number

if num1 > num2 and num1 > num3:
    print("The largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is", num2)
else:
    print("The largest number is", num3)
