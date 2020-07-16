"""
    Numpy : Numerical Python
    Reference Library Link: https://numpy.org/

    For entering into the world of Data Science
    You must know below libraries as baseline fundamentals:
    1. NumPy                    | Data Structure and computation on the same
    2. MatplotLib/Seaborn       | Data Visualization
    3. Pandas                   | Data Analysis

    Why NumPy ? To have mathematical Statistical Operations

"""

import numpy as np

# 1. Creating Arrays
#    Arrays are dynamic :)
#    They are kind of Lists in Python BUT, they are more Optimized (Less Time and Less Memory)

numbers = [1, 2, 3, 4, 5]
print(numbers)  # will have , as separator in output display

# Creating 1-D
array_1_d = np.array([1, 2, 3, 4, 5])
print(array_1_d)  # will have space ' ' as separator in output display

# Printing the Dimensions of Array
print(array_1_d.ndim)   # a number for dimension
print(array_1_d.shape)  # shape as tuple -> (5,) 5 elements in one single row

print(array_1_d.nbytes) # memory 40 bytes of data | 8 byte
print(array_1_d.data)   # memory HashCodes

array_2_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(array_2_d)
print(array_2_d.ndim)       # 2 -> Array of Arrays
print(array_2_d.shape)      # (3, 3)

array_2_d_jagged = np.array([
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
])

print(array_2_d_jagged)         # Prints array of python lists
print(array_2_d_jagged.ndim)    # 1
print(array_2_d_jagged.shape)   # (3,)

array_3_d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
])

print(array_3_d)
print(array_3_d.ndim)   # 3
print(array_3_d.shape)  # 2, 3, 3


# array_with_dt = np.array([1.1, 2.2, 3.3], dtype=float)
array_with_dt = np.array([1, 2, 3], dtype=float)
print(array_with_dt)
print(array_with_dt.dtype)
