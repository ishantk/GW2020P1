"""
    Broadcasting:
        Important Term used in Machine Learning
        As many a times mathematically we may need to perform some mathematical operations on different shaped arrays
"""

import numpy as np
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

print("X IS: ")
print(X)
print(X.shape)

print()

vector = np.array([1, 0, 1])
print("vector is: ")
print(vector)
print(vector.shape)

Y = np.empty_like(X)
print("Y is: ")
print(Y)
print(Y.shape)

print(len(X)) # 4

for i in range(len(X)):
    Y[i, :] = X[i, :] + vector

print("Y after Addition is: ")
print(Y)
print(Y.shape)


A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [2],
    [4],
    [6]
])

print("A is: ")
print(A)
print(A.shape)

print("B is: ")
print(B)
print(B.shape)


print("matrix_broadcasted is: ")
matrix_broadcasted = A + B
print(matrix_broadcasted)
print(matrix_broadcasted.shape)