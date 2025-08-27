"""
🎯 Program Description:
-----------------------
This program simulates an ATM PIN verification system using a `for` loop.

✅ Goals:
- Allow the user to enter their 4-digit PIN.
- Give a maximum of 3 attempts to enter the correct PIN.
- If the PIN is correct, display "Access Granted" and exit.
- If the PIN is incorrect:
    → Warn the user how many attempts are left.
    → After 3 incorrect attempts, display "Card Blocked!".
- Demonstrates use of:
    - `for` loop with range
    - `if-else` conditions
    - Loop control using `break`
    - Basic user input and string comparison
"""
# Define the correct PIN to compare against user input
correct_pin = "1234"

# Use a for loop to allow the user up to 3 attempts to enter the correct PIN
for attempt in range(1, 4):  # 3 attempts
    # Ask the user to enter their 4-digit PIN
    entered_pin = input("Enter your 4-digit ATM PIN: ")
    
    # Check if the entered PIN matches the correct PIN
    if entered_pin == correct_pin:
        print("Access Granted")
        break  # exit the loop
    else:
        # If the attempt is less than 3, show how many attempts are left
        if attempt < 3:
            print("Wrong PIN. You have", 3 - attempt, "attempt(s) left.")
        # If this is the third wrong attempt, block the card
        else:
            print("Wrong PIN entered 3 times.")
            print("Card Blocked!")
