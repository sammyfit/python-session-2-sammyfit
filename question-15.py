# List of items added to the cart
cart_items = ["apple", "chocolate", "milk", "out-of-stock", "bread", "alcohol", "eggs"]

print("🛒 Processing your cart...")

for item in cart_items:  # Loop through cart items
    if item == "out-of-stock":
        continue  # Skip this item
    
    if item == "alcohol":
        print("⚠️ Restricted item detected:", item)
        print("Checkout stopped!")
        break  # Stop the loop

    print("✔️ Added to final list:", item)
