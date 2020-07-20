import numpy as np

"""
    DOT PRODUCT
    M1      M2          M3
    [a   b] [e  f]      [ae + bg    af + bh]
    [c   d] [g  h]      [ce + dg    cf + dh]

"""

matrix_1 = np.array([
    [2, 3],
    [1, 4],
])

matrix_2 = np.array([
    [2, 3],
    [1, 6],
])

result = np.dot(matrix_1, matrix_2)
print(result)

# linalg : Linear Algebra
det_matrix_1 = np.linalg.det(matrix_1)
print(det_matrix_1)

# np.linalg.det()
# np.linalg.inv()
# np.linalg.norm()
# and more...
# you can work on majorly all the mathematical functions with numpy