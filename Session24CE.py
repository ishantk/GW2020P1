# Arithmetic Operations
import numpy as np
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("SUM is:")
SUM = A + B
print(SUM)
print(SUM.shape)

print()

print("DIFF is:")
DIFF = A - B
print(DIFF)
print(DIFF.shape)

print()

print("MUL is:")
MUL = A * B
print(MUL)
print(MUL.shape)

print()

print("DIV is:")
DIV = A / B
print(DIV)
print(DIV.shape)

print()

C = A + 5
D = B * 2

print("C is:")
print(C)
print("D is:")
print(D)

print()
sqrt = np.sqrt(A)
print("SQRT of A is: ")
print(sqrt)

exp = np.exp(A)
print("EXP of A is: ")
print(exp)