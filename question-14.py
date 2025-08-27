"""
Upgrading Store from Fixed Price Toys to Variable Price Toys
"""

toy_cart = []

customer_name = input('Enter Customer Name: ')
quantity = int(input('Enter number of different toys purchased by customer: '))

for each_toy in range(0, quantity):
    print(f"\nEnter details for Toy #{each_toy + 1}:")
    toy_name = input("Toy Name: ")
    toy_price = float(input("Toy Price (INR): "))
    toy_qty = int(input("Quantity: "))

    toy_details = {
        "toy_name": toy_name,
        "toy_price": toy_price,
        "toy_quantity": toy_qty
    }

    toy_cart.append(toy_details)

total_amount = 0

print('\n---------------------------- Invoice Details ----------------------------')
print('Shop Name      : The Toy Store')
print(f'Customer Name  : {customer_name}\n')
print(f'{"Toy Name":<16}{"Price":<12}{"*":<3}{"Qty":<8}{"=":<3}{"Subtotal"}')
print('-' * 72)

for toy in toy_cart:
    toy_sub_total = toy['toy_price'] * toy['toy_quantity']
    total_amount += toy_sub_total
    print(f"{toy['toy_name']:<16}{toy['toy_price']:<12.2f}* {toy['toy_quantity']:<7}= {toy_sub_total:.2f}")

if total_amount < 5000:
    discount = 2
elif total_amount >= 5000 and total_amount <= 10000:
    discount = 5
elif total_amount > 10000:
    discount = 10
else:
    discount = 0

if total_amount > 5000:
    product_tax = 2
else:
    product_tax = 0

discount_amount = (total_amount * discount) / 100
tax_amount = (total_amount * product_tax) / 100

discounted_total_amount = total_amount - discount_amount + tax_amount

print('-' * 72)
print(f'{"Total Amount":<40}{total_amount:>20.2f}')
print(f'{"Discount Amount":<40}-₹{discount_amount:>19.2f}')
print(f'{"Tax Amount":<40}+₹{tax_amount:>19.2f}')
print('-' * 72)
print(f"\n{customer_name} spent a total of ₹{discounted_total_amount:.2f} after applying {discount}% discount.")
