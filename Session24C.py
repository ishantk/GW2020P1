# Indexing and Slicing in Array
import numpy as np

X = np.arange(1, 11)
print(X)

# Index Access -> Update Operation
X[0] = 12
X[9] = 99

print(X)
print(X[9])

# del wont be supported
# del X[9]

# extracting selective elements from Array
print(X[2:6]) # from 2 to 5
print(X[3:])  # from 3 to len of X
print(X[:5])  # form 0 to 4

# Slicing on Multiple Indexes
print(X[1:7:3])

print(X[-5:9])

# Boolean Indexing
print(X[X>5]) # elements in the Array > 5
# Try more conditional operators above

print()

# Indexing in Multi-Dimensional Arrays
Y = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])
print(Y)
print()
print(Y[0:2, 1:2])
print()
print(Y[[0, 1, 2], [0, 0, 1]])
