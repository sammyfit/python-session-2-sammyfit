"""
🎯 Program Description:
-----------------------
This program counts how many even and odd numbers exist between 1 and 100 (inclusive).

✅ Goals:
- Use a `for` loop to iterate from 1 to 100
- Use the modulo operator `%` to check if a number is even or odd
- Keep separate counts of even and odd numbers using two counters
- Print the total count of even and odd numbers at the end

🧠 Concepts Covered:
- `for` loop with `range()`
- Conditional statements (`if-else`)
- Modulo operation (`%`)
- Variable incrementing (`+= 1`)
"""

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through numbers from 1 to 100
for num in range(1, 101):  
    # Check if the number is even
    if num % 2 == 0:
        even_count += 1  # Increase even counter
    else:
        odd_count += 1   # Increase odd counter

# Display the result
print("Even Count:", even_count)
print("Odd Count:", odd_count)
