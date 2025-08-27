"""
Program: Simple Bank Transaction Simulator

Description:
------------
This program simulates a bank account transaction system that allows a user to 
perform debit or credit operations on their account.

Steps:
------
1. Accept initial account balance from the user.
2. Ask the user for the operation type: 'debit' or 'credit'.
3. Accept transaction amount from the user.
4. Process the transaction:
    - For debit: Check for sufficient balance.
    - For credit: Add the amount to the balance.
5. Display the transaction result and updated account balance.
"""

# Get initial balance from user
balance = float(input("Enter Initial Balance: "))  # Enter initial balance (float)

# Ask user for operation type
operation = input("Enter debit or credit: ")  # Enter 'debit' or 'credit'

# Get transaction amount
amount = float(input("Enter transaction amount: "))  # Enter transaction amount (float)

# Perform transaction based on operation
if operation == 'debit':
    if amount <= balance:
        balance -= amount   # Subtract amount from balance
        print("Debit Successful! ₹", amount, "debited.")
    else:
        print("Insufficient Balance! Debit Failed.")
elif operation == 'credit':
    balance += amount  # Add amount to balance
    print("Credit Successful! ₹", amount, "credited.")
else:
    print("Invalid Operation Selected.")

# Show final balance
print("Updated Account Balance: ₹", balance)
