def second_third_largest(lst):
    sorted_list = sorted(lst, reverse=True)
    print("Second Largest:", sorted_list[1])
    print("Third Largest:", sorted_list[2])

nums = [100, 5, 98, 10, 2, 1, 43, 62]
second_third_largest(nums)
