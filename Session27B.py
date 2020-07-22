import matplotlib.pyplot as plt


X = list(range(0, 11))
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

# plt.plot(X, Y1, label="Y1")
# plt.plot(X, Y2, label="Y2")
# plt.plot(X, Y3, label="Y3")

# plt.plot(X, Y1, "y", label="Y1")
# plt.plot(X, Y2, "m", label="Y2")
# plt.plot(X, Y3, "black", label="Y3")

# plt.plot(X, Y1, "o", label="Y1")
# plt.plot(X, Y2, "^", label="Y2")
# plt.plot(X, Y3, "D", label="Y3")

plt.plot(X, Y1, ".", label="Y1", color="black")
plt.plot(X, Y2, "-.", label="Y2", color="y")
plt.plot(X, Y3, ":", label="Y3", color="m")

plt.legend()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graphs")

plt.show()

# PS: Geographical Maps                       | https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
#     Do Explore SeaBorn Library for Graphing | https://seaborn.pydata.org/tutorial.html
