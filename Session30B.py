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

another_data_set = {
    "teams": ["Sunrisers Hyderabad", "Mumbai Indians", "Pune Warriors"],
    "ranks": [8, 9, 5],
    "years": [2015, 2019, 2018]
}

table1 = pd.DataFrame(ipl_data_set)
table2 = pd.DataFrame(another_data_set)

print("Table1:")
print(table1)

print("Table2:")
print(table2)

# Implement Merging of Tables
# Please review joins first on the SQL Tables: https://www.w3schools.com/sql/sql_join.asp

# table3 = pd.merge(table1, table2, on="teams", how="left")
table3 = pd.merge(table1, table2, on="teams", how="right")
# table3 = pd.merge(table1, table2, on="teams", how="inner")
# table3 = pd.merge(table1, table2, on="teams", how="outer")

print("Table3:")
print(table3)