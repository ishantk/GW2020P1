import numpy as np

numbers1 = (10, 20, 30, 40, 50)
numbers2 = [10, 20, 30, 40, 50]
numbers3 = {10, 20, 30, 40, 50}
numbers4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
name = "john"

array1 = np.array(name)

print(name, type(name))
print(array1, type(array1))

# PS: The possible data structures which holds data in Python, can be converted to numpy nd array
#     Explore if object constructed by us can be converted to numpy array or not :)


