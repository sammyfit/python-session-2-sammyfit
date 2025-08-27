"""
Program: Online Food Delivery Charge & Discount Calculator

Description:
------------
This program calculates:
1. Delivery charge based on delivery distance.
2. Discount based on order amount.
3. Total amount payable after adding delivery charges and applying discount.

Delivery Charge Slabs:
----------------------
- Up to 5 km           → ₹20
- 6 km to 10 km        → ₹50
- Above 10 km          → Delivery Not Available

Discount Slabs:
---------------
- ₹500 to ₹999         → 10% discount on order amount
- ₹1000 or more        → 20% discount on order amount
"""

# Get delivery distance and order amount
distance = float(input("Enter a valid distance in kms: "))  # Enter distance in km (float)
order_amount = float(input("Enter amount of the order: ")) # Enter order amount (float)

# Calculate delivery charge
if distance <= 5:
    delivery_charge = 20
elif distance > 5 and distance <= 10:
    delivery_charge = 50
else:
    print("Delivery Not Available for distance above 10 km.")
    delivery_charge = None  # No delivery, no need to proceed

# Continue only if delivery is available
if delivery_charge is not None:
    # Calculate discount
    if order_amount >= 1000:
        # provide 20% discount if order amount is more than 1000
        discount = (order_amount * 20) / 100
    elif order_amount >= 500:

        discount = (order_amount * 10) / 100
    else:
        discount = 0

    # Calculate final amount
    total_amount = order_amount + delivery_charge - discount

    # Display results
    print("\nOrder Amount: ₹", order_amount)
    print("Delivery Charge: ₹", delivery_charge)
    print("Discount Applied: ₹", discount)
    print("Total Payable Amount: ₹", total_amount)
