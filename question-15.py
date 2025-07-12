# List of items added to the cart
cart_items = ["apple", "chocolate", "milk", "out-of-stock", "bread", "alcohol", "eggs"]

print("🛒 Processing your cart...")

for item in __________:  # Loop through cart items
    if item == "out-of-stock":
        __________  # Skip this item
    
    if item == "alcohol":
        print("⚠️ Restricted item detected:", item)
        print("Checkout stopped!")
        __________  # Stop the loop

    print("✔️ Added to final list:", item)
