import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 11)
Y1 = np.sin(X)
Y2 = np.tan(X)

print(X)
print(Y1)
print(Y2)

plt.plot(X, Y1, label="sin")
plt.plot(X, Y2, label="tan")

plt.legend()

plt.show()