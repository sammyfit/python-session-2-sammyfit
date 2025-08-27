numbers = [3, -2, 7, -1, 5]

print("Only positive numbers:")

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(num)
