"""
    Introduction to Pandas
    Data Analysis Library
    Refernce Link: https://pandas.pydata.org/
    Cheat Sheet:   https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
"""

import pandas as pd
import numpy as np

print(pd.__version__)

# 1-D Array
series = pd.Series()

# 2-D Array
frame = pd.DataFrame()

print(series, type(series))
print(frame, type(frame))

numbers1 = [10, 20, 30, 40, 50]     # List
numbers2 = np.arange(11, 51, 10)    # ndarray

series1 = pd.Series(numbers1)
series2 = pd.Series(numbers2)

print(numbers1)
print(numbers2)
print(series1)
print(series2)

employee = {"name": "John", "age": 22, "salary": 35001.85}
series3 = pd.Series(employee)
print(series3)


print("===Accessing Data in Series===")
print(series1[0])
print(series2[1])
print(series3["age"])

print("===Updating Data in Series===")
series1[1] = 111
series2[2] = 222
series3["name"] = "John Watson"

print(series1)
print(series2)
print(series3)

print("===Slicing Data in Series===")
print(series1[1:3])
print(series2[2:4])
print(series3["name":"age"])
print(series3["name":])

print("===Deleting Data in Series===")
del series1[0]
print(series1)

print("===Appending Data in Series===")
series1[50] = 99
print(series1)

series3["email"] = "john.watson@example.com"
print(series3)