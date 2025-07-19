main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to find: ")

index = main_str.find(sub_str)
count = main_str.count(sub_str)

if index != -1:
    print(f"Substring found at index {index}")
    print(f"Substring appears {count} times")
else:
    print("Substring not found")
