import numpy as np
data = [
    (8, 9),
    (10, 18),
    (13, 14),
]


array1 = np.array(data)
print(array1)
print(array1[0:2, 1])

print(array1.min())
print(array1.max())
print(array1.sum())

# Axis: 0 -> Columns
# Axis: 1 -> Rows
print("Column Wise Min and Max")
print(array1.min(axis=0))
print(array1.max(axis=0))

print("Row Wise Min and Max")
print(array1.min(axis=1))
print(array1.max(axis=1))