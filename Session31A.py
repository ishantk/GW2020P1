import pandas as pd
import matplotlib.pyplot as plt

"""
    1. Plot Total Sales per month in year 2011
       How the total sales has increased over the months in year 2011
       which month has the lowest sales ?
       
"""

table = pd.read_csv("BigMartSalesData.csv")
print(table)

print("Data for Year 2011")
table_year_2011 = table[table['Year'] == 2011]
print(table_year_2011)

print("Group Data Month Wise for Year 2010")
sales_year_2011_data_monthly = table_year_2011.groupby('Month').sum()['Amount']
print(sales_year_2011_data_monthly)

print("Lowest Sales {} recorded in month {}".format(sales_year_2011_data_monthly.min(), sales_year_2011_data_monthly.idxmin()))
print("Highest Sales {} recorded in month {}".format(sales_year_2011_data_monthly.max(), sales_year_2011_data_monthly.idxmax()))

min_value = pd.Index(sales_year_2011_data_monthly).min()
max_value = pd.Index(sales_year_2011_data_monthly).max()

print("min_value is:", min_value)
print("max_value is:", max_value)

plt.plot(sales_year_2011_data_monthly.index, sales_year_2011_data_monthly.values)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Big Mart 2011 Sales Report")
plt.show()