"""
🎯 Program Description:
-----------------------
This program simulates a billing system for a toy store using basic arithmetic and conditional logic in Python.

✅ What the program does:
- Asks the user to input their name and the number of toys purchased.
- Calculates the total cost based on a fixed toy price.
- Applies a discount based on the quantity of toys purchased:
    - < 5 toys  → 2% discount
    - 5–10 toys → 5% discount
    - > 10 toys → 10% discount
- Adds an additional 2% tax if more than 50 toys are purchased.
- Calculates:
    - Total price before discount
    - Discount amount
    - Tax amount
    - Final payable amount after discount and tax
- Prints a friendly billing summary showing all the above.

🧠 Concepts Covered:
- User input and type casting
- Conditional statements (if-elif-else)
- Arithmetic calculations (%, *, +, -)
- f-strings for clean output formatting
"""

# Fixed price of each toy in INR
toy_price = 100

# Discount Percentage (initial value)
discount = 2

# Name of the customer
customer_name = input('Enter Customer Name : ')

# Number of toys purchased by the customer
quantity = ____('Enter Quantity of toys purchased by customer: ')

# typecast quantity from string to integer
quantity = ____(quantity)

# Calculate total amount spent by the customer before any discount
total_amount = toy_price * quantity

# Apply discount based on quantity purchased
if quantity ___ 5:
    discount = 2
elif quantity > 5 ____ quantity < 10:
    discount = 5
elif quantity > 10:
    discount = 10
else:
    discount = 0

# Apply tax only if quantity is more than 50
if quantity > 50:
    _____ = 2
else:
    product_tax = ____ # add zero tax for simplicity

# Calculate discount and tax amounts
discount_amount = (total_amount * discount) / 100
tax_amount = (total_amount * product_tax) / 100

# Calculate final amount after applying discount and tax
discounted_total_amount = total_amount - discount_amount + tax_amount

# Display the total billing summary
print('\n---------Welcome to toy store---------')
print(f'Total Amount is {total_amount}')
print(f'Discount Amount is -{discount_amount}')
print(f'Tax Amount is +{tax_amount}')
print(f"\n{customer_name} spent a total on toys after {discount}% discount is {discounted_total_amount}")
