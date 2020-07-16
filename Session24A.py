import numpy as np

# Some more ways to create Arrays

# zeros_array = np.zeros(3) # zeros is by default float
zeros_array_1d = np.zeros(3, dtype=int)
print(zeros_array_1d)

zeros_array_2d = np.zeros((3, 3), dtype=int)
print(zeros_array_2d)

ones_array_1d = np.ones(3, dtype=int)
print(ones_array_1d)

ones_array_2d = np.ones((3, 3), dtype=int)
print(ones_array_2d)

# Chessboard: 8 X 8 Matrix of Black and White | 1 and 0
chessboard = np.ones((8, 8), dtype=int)
print("---CHESSBOARD---")
print(chessboard)

# we can write Loops on Numpy Arrays
for i in range(0, len(chessboard)):

    for j in range(0, len(chessboard)):
        print(chessboard[i][j], end=" ")

    print()

# Range Arrays
# range_array = np.arange(5, 11)
range_array = np.arange(1, 21, 3)
print(range_array)

# Assignment: how 0's can be placed alternatively on the Chessboard using numpy array or slicing technique
#             Explore Enhanced For Loop on Numpy Array | for element in chessboard:
#             Explore if we can have 2D Arrays created with Range Function :) 