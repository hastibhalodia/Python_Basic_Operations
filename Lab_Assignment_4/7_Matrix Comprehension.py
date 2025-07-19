# 3x3 matrix
matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Last column
last_col = [row[-1] for row in matrix3]
print("Last column:", last_col)

# Two 2x2 matrices
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]

# Element-wise sum
sum_matrix = [[mat1[i][j] + mat2[i][j] for j in range(2)] for i in range(2)]
print("Element-wise sum of 2x2 matrices:", sum_matrix)
