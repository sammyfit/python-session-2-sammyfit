"""
Program: Employee Tax Slab Calculator

Description:
------------
This program calculates the tax slab and expected tax amount for an employee
based on their annual salary using if-elif-else conditions.

Tax Slabs:
-----------
| Annual Salary Range         | Tax Slab | Tax Rate |
|----------------------------------|------------|------------|
| Up to ₹2,50,000                 | No Tax   | 0%          |
| ₹2,50,001 to ₹5,00,000    | 5%          | 5%          |
| ₹5,00,001 to ₹10,00,000  | 20%        | 20%       |
| Above ₹10,00,000             | 30%        | 30%       |

Instructions:
-------------
1. Accept employee name and annual salary from user input.
2. Identify the correct tax slab based on the annual salary.
3. Calculate the expected tax amount.
4. Display the results clearly.
"""

# Get employee details
employee_name = ____  # Input employee name
annual_salary = ____  # Input annual salary (float)

# Determine tax slab and calculate tax
if annual_salary <= 250000:
    tax_rate = 0
elif annual_salary ____ 250000 and annual_salary <= 500000:
    tax_rate = 5
elif annual_salary ____ 500000 ___ annual_salary <= 1000000:
    tax_rate = 20
else:
    tax_rate = 30

# Calculate tax amount
expected_tax = (annual_salary * tax_rate) / 100

# Display results
print("\nEmployee Name:", employee_name)
print("Annual Salary: ₹", annual_salary)
print("Tax Slab:", tax_rate, "%")
print("Expected Tax Amount: ₹", expected_tax)
