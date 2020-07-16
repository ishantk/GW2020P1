# Shapes of Arrays

import numpy as np
my_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(my_array)
print(my_array.shape)

print()

my_array = my_array.reshape(3, 2)
print(my_array)
print(my_array.shape)

print()

array_3_d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
])

print(array_3_d)
print(array_3_d.shape)

# collectively explore
# array_3_d = array_3_d.resize()
# print(array_3_d)
