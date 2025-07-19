def modify_list():
    lst = [5, 3, 9, 5, 5, 5, 0]
    print("Original List:", lst)

    # i. Insert 99 at 3rd position (index 2)
    lst.insert(2, 99)
    print("After inserting 99 at index 2:", lst)

    # ii. Remove all alternate elements starting from index 1
    lst = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    print("After removing alternate elements:", lst)

    # iii. Count occurrences
    for item in set(lst):
        print(f"Element {item} appears {lst.count(item)} times")

    # iv. Sort ascending and descending
    asc = sorted(lst)
    desc = sorted(lst, reverse=True)
    print("Ascending:", asc)
    print("Descending:", desc)

    # v. Last element using positive and negative indexing
    print("Last element (+ve index):", lst[len(lst)-1])
    print("Last element (-ve index):", lst[-1])

modify_list()
