import pandas as pd
import numpy as np

oddNumbers = np.arange(1, 100, 2)
evenNumbers = np.arange(0, 100, 2)

numbers = {"oddNumbers": oddNumbers, "evenNumbers": evenNumbers}

table = pd.DataFrame(numbers)
print(table)

print("SUM")
print(table.sum())

print("MAX")
print(table.max())

print("MIN")
print(table.min())

print("STD")
print(table.std()) # Standard Deviation | Ref: https://www.mathsisfun.com/data/standard-deviation-formulas.html