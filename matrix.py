matrix_a = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

matrix_b = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

result = [[0 for _ in range(5)] for _ in range(5)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
        for k in range(len(matrix_b)):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

for row in result:
    print(row)
    
    
    
import numpy as np

matrix_a = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]])

matrix_b = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]])
result_at = matrix_a @ matrix_b
result_matmul = np.matmul(matrix_a, matrix_b)
print("Matrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)
print("\nResult (A @ B):\n", result_at)