s = input("Enter a string: ")

# Swap first 3 and last 3
if len(s) >= 6:
    new_str = s[-3:] + s[3:-3] + s[:3]
    print("Swapped string:", new_str)
else:
    print("String too short to swap 3 characters")

# Remove first and last character
print("Without first and last character:", s[1:-1])
