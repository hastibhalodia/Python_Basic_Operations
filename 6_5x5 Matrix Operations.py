matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Row-wise
def row_wise(matrix):
    print("Row-wise:")
    for row in matrix:
        print(row)

# Column-wise
def column_wise(matrix):
    print("Column-wise:")
    for col in range(5):
        for row in matrix:
            print(row[col], end=" ")
        print()

# Second and Last Row
def specific_rows(matrix):
    print("Second Row:", matrix[1])
    print("Last Row:", matrix[-1])

# Diagonal & Off-diagonal
def diagonals(matrix):
    print("Diagonal elements:", [matrix[i][i] for i in range(5)])
    print("Off-diagonal elements:", [matrix[i][4-i] for i in range(5)])

row_wise(matrix)
column_wise(matrix)
specific_rows(matrix)
diagonals(matrix)
