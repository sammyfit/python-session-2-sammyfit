"""
Program: Player Availability Checker - Indian Cricket Team

Description:
------------
This program checks whether a given player is part of the Indian cricket team's Playing 11.
It uses a Python list to store the names of the players.

The program:
1. Asks the user to enter a player's name.
2. Checks if the entered player is present in the Playing 11 list using the membership operator 'in'.
3. Displays an appropriate message showing whether the player is part of the Playing 11 or not.

This program demonstrates:
- Use of Python lists
- Membership operator ('in')
- if-else statements
- User input handling
"""

# List of Playing 11 Players for Indian Cricket Team
playing_11 = ['Rohit Sharma', 'Shubman Gill', 'Virat Kohli', 'Shreyas Iyer', 
              'KL Rahul', 'Hardik Pandya', 'Ravindra Jadeja', 
              'Kuldeep Yadav', 'Jasprit Bumrah', 'Mohammed Siraj', 'Mohammed Shami']

# Ask user to enter player name
player = ____  # Input player name from user

# Check if player is in Playing 11
if player ___ playing_11:   # Check membership in list
    print(player, "=> Yes, in Playing 11")
else:
    print(player, "=> No, not in Playing 11")
