import pandas as pd
import numpy as np

# Generate Random Numbers with 5 rows and 4 columns :)
data = np.random.randn(5, 4)
print(data)
print(data.shape)

table = pd.DataFrame(data=data, columns=["COL1", "COL2", "COL3", "COL4"])
print(table)

print("COLUMN2 Data")
print(table["COL2"])

print("COLUMN3 Data")
print(table.COL3)

print()

print("ITERATE in DATAFRAME - 1")
# iteritems() => Iterate Column Wise
for key, value in table.iteritems():
    print(key)
    print("*******")
    print(value)
    print("=======")

print()
print("ITERATE in DATAFRAME - 2")
# iterrows() => Iterate Row Wise
for key, value in table.iterrows():
    print(key)
    print("*******")
    print(value)
    print("=======")


print("ITERATE in DATAFRAME - 3")
# itertuples() => Iterate as Tuples
for row in table.itertuples():
    print(row)
    print("*******")