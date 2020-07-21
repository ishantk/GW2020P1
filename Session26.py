"""
    Data Visualization with Matplotlib
    https://matplotlib.org/
"""

# import matplotlib as lib
# print(lib.__version__) # to check the installed version of your library

import matplotlib.pyplot as plt

"""
data = [0, 1, 2, 3, 4, 5]
plt.plot(data)  # plot plots a line graph
plt.show()
"""

X = list(range(0, 11))
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print("X:", X)
print("Y1:", Y1)
print("Y2:", Y2)
print("Y3:", Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graphs")

plt.grid(True)

# plt.xlim(0, 20)
# plt.ylim(0, 20)

plt.savefig("MyGraph")

plt.show()



