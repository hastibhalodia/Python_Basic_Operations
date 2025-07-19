matrix3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose using zip and list comprehension
transpose = [list(row) for row in zip(*matrix3x3)]
print("Transposed Matrix:")
for row in transpose:
    print(row)
