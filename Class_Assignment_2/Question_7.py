s = input("Enter a string: ")

# Remove middle character
middle_index = len(s) // 2
if len(s) % 2 == 0:
    removed_middle = s
else:
    removed_middle = s[:middle_index] + s[middle_index+1:]
print("Without middle character:", removed_middle)

# Reverse with every second character
print("Reverse string with every second character:", s[::-2])

# Substring from index 2 to 8
print("Substring from index 2 to 8:", s[2:8])

# Substring from middle to end
print("Substring from middle to end:", s[len(s)//2:])