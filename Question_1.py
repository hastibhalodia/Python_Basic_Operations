# Accept a floating-point number
num = float(input("Enter a floating-point number: "))

# Using built-in functions
print("Rounded value:", round(num))
print("Integer value:", int(num))
print("Absolute value:", abs(num))

# Explanation
# round() rounds the number to the nearest integer (example: 4.6 -> 5, 4.4 -> 4)
# int() just removes the decimal part without rounding (example: 4.9 -> 4)
# abs() gives the positive version of the number

# Accepting a list of integers
nums = list(map(int, input("Enter a list of integers separated by space: ").split()))

# Using max, min, sum
print("Largest number:", max(nums))
print("Smallest number:", min(nums))
print("Sum of all numbers:", sum(nums))
