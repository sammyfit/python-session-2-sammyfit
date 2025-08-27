"""
Assignment: Age-based Permission Checker (Syntax + Logic Practice)

Description:
------------
This program checks various permissions based on:
1. Gender (male/female)
2. Age

Permissions:
- Driving License (Age >= 18)
- Marriage (Male: 21+, Female: 18+)
- Voting (Age >= 18)
- Senior Citizen Benefits (Age >= 60)

Instructions:
-------------
Fill in all the blanks (marked as ____). 
All blanks cover syntax, function, operators, and logic.
"""

# Take user input
gender = input("Enter your gender (male/female): ").lower()
age = int(input("Enter your age: "))

# Main permission checks using nested if-else & 'or'
if age >= 18:
    print("Eligible for Driving License.")
    print("Eligible for Voting Rights.")
    
    if (gender == 'male' and age > 21) or (gender == 'female' and age > 18):
        print("Eligible for Marriage.")
    else:
        print("Not eligible for Marriage yet.")
    if age >= 60:
        print("Eligible for Senior Citizen Benefits.")
    else:
        print("Not eligible for Senior Citizen Benefits.")
        
else:
    print("Not eligible for Driving License or Voting Rights.")
    print("Not eligible for Marriage")
    
    print("Too young for Senior Citizen Benefits.")
