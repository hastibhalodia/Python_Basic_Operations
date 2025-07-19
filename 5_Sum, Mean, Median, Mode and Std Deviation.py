import statistics

def stats_operations(lst):
    print("Original List:", lst)
    print("Sum:", sum(lst))
    print("Mean:", statistics.mean(lst))
    print("Median:", statistics.median(lst))
    print("Mode:", statistics.mode(lst))

    # Reverse using slicing
    rev = lst[::-1]
    print("Reversed List:", rev)
    print("Mean (Reversed):", statistics.mean(rev))
    print("Median (Reversed):", statistics.median(rev))
    print("Mode (Reversed):", statistics.mode(rev))
    print("Standard Deviation (Reversed):", statistics.stdev(rev))

stats_operations([100, 5, 98, 10, 2, 1, 43, 62])