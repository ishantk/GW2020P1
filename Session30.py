"""
    Pandas Part-II
"""

import pandas as pd

teams = [
    "Rajasthan Royals",
    "Delhi Capitals",
    "Chennai Super Kings",
    "Mumbai Indians",
    "Delhi Capitals",
    "Kolkata Knight Riders",
    "Chennai Super Kings",
    "Deccan Chargers",
    "Kings XI Punjab",
    "Mumbai Indias"
]

ranks = [2, 3, 4, 1, 3, 4, 1, 2, 5, 4]
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

ipl_data_set = {
    "teams": teams,
    "ranks": ranks,
    "years": years
}

print(ipl_data_set)
# Assignment: Web-scarap the above data set :)

print()

data_set = pd.DataFrame(ipl_data_set)
print(data_set)

print()

grouped_data_set = data_set.groupby('ranks')
# print(grouped_data_set)
print(grouped_data_set.groups)

print()

grouped_data_set = data_set.groupby(['teams', 'ranks'])
print(grouped_data_set.groups)

print()

print("****Iterating In Group****")
for team_name, grp in grouped_data_set:
    print(grp)
    print(team_name)
    print("-------------------------------")


print("****Fetching Single Group****")
print(grouped_data_set.get_group("Mumbai Indias"))
# Please read the thread and see if we have done something wrong: https://github.com/pandas-dev/pandas/issues/8121
