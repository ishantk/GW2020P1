import numpy as np

array = np.loadtxt("data.txt", dtype=np.int)
print(array)

my_array = np.arange(10, 200, 10)
print(my_array)

np.savetxt("mydata.txt", my_array, fmt="%04d")
print("mydata.txt saved with my_array content")