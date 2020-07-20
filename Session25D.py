
import numpy as np

X = np.array([
    (1, 2, 3),
    (4, 5, 6)
])

Y = np.array([
    (1, 2, 3),
    (4, 5, 6)
])

print(X)
print(Y)

print("VStack")
v_stack = np.vstack((X, Y))
print(v_stack)

print("HStack")
h_stack = np.hstack((X, Y))
print(h_stack)

Z = np.arange(1, 101, 10)
print(Z)
print(np.log10(Z))
print(np.sin(Z))
print(np.exp(Z))

