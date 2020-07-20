"""
    More of Numpy
"""

import numpy as np
array = np.arange(10, 51, 2)
print(array)


indexes = slice(1, 20, 2)
print(indexes)
# print(list(indexes)) # error

print(array[1:20])
print(array[1:20:2])
print(array[indexes])
