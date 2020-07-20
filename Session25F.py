import numpy as np
array = np.genfromtxt("CityTemps.csv", delimiter=",")
print(array)

print(array[0])
print(array[1])
print(array[1][0])

# Data Analysis Assignment:
# Compute the Results below and share the code in group
# 1. How many years in total we have in the data : 2, 2104 and 2015
# 2. City Wise Min and Max Temp
# 3. City Wise Min and Max Temp along with Month and Year
# 4. Sort the Months as per temp
# 5. Explore more data sets on Kaggle