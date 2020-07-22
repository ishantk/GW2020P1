import matplotlib.pyplot as plt
import numpy as np

X1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y1 = [11, 7, 8, 12, 33, 12, 6, 4, 39, 32]

X2 = np.random.randn(20)
Y2 = np.random.randn(20)

plt.scatter(X1, Y1, label="Country1")
plt.scatter(X2, Y2, label="Country2")
plt.legend()
plt.show()