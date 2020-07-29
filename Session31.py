"""
    soccerdata analysis with pandas to find best goal keeper :)
"""

import pandas as pd

import matplotlib.pyplot as plt # so as to use seaborn
import seaborn as sns # Reference Link: https://seaborn.pydata.org/tutorial.html

table = pd.read_csv("soccerdata.csv")
print(table)

# print(table.head()) # top 5
print(table.head(10)) # top 10

print(table.Name) # OR print(table['Name'])

# sns.countplot(y=table.Nationality, palette="Set2")
# sns.countplot(x="Age", data=table)
# sns.countplot(x="Nationality", data=table)

# Format titles on X and Y axis of your graph to show them properly
# hint : names may fit in well if put up diagonally /

# plt.show()

# Case Study: Finding goalkeepers who are sort of best to stop the goals
# extract the attributes from which we can draw a decision
# weight them according to their importance

# example:
w1 = 1
w2 = 2
w3 = 3
w4 = 4

# associate the above weights to the attributes as per the importance
table["GK_SCORE"] = w1*table.GK_Positioning + w2*table.GK_Diving + w3*table.GK_Handling + w4*table.GK_Reflexes

print(table)

sorted_table = table.sort_values("GK_SCORE")
print(sorted_table)

print(sorted_table.tail(10))