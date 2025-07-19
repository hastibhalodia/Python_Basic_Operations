cities = ["Mumbai", "Delhi", "Ahmedabad", "Kolkata", "Bangalore"]

print("Cities List:", cities)
print("Length of list:", len(cities))
print("Type of list:", type(cities))
print("Type of each element:")
for city in cities:
    print(city, "->", type(city))

# Accessing with indexing
print("First city (positive index):", cities[0])
print("Last city (negative index):", cities[-1])