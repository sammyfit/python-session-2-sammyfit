"""
Program: Food Order Availability Checker

Description:
------------
This program allows the user to select one food item from the given menu.
It then checks whether the selected food item belongs to the Veg or Non-Veg menu,
and identifies the user's food preference:
- If the item is from Veg menu → user is Vegetarian.
- If the item is from Non-Veg menu → user is Non-Vegetarian.
- If the item does not exist in either menu → shows invalid choice.
"""

# Display menu
print("Enter one option for food type from the below list")
user_choice = input("paneer, dal, chole, chicken, fish, mutton: ")

# Food menus
veg_menu = ['paneer', 'dal', 'chole']
non_veg_menu = ['chicken', 'fish', 'mutton']

# Check food type and display result
if user_choice ____ veg_menu:
    print("User is Vegetarian.")
elif ____ in ____:
    print("User is Non-Vegetarian.")
else:
    print("Invalid choice, please try again.")
