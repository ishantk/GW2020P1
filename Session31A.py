import pandas as pd
import matplotlib.pyplot as plt

"""
    1. Plot Total Sales per month in year 2011
       How the total sales has increased over the months in year 2011
       which month has the lowest sales ?
       
"""

def sales_plot():

    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print("Data for Year 2011")
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    print("Group Data Month Wise for Year 2011")
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

"""
    2. Plot Total Sales per month in year 2011 on a Bar Graph  
"""


def bar_plot():

    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print("Data for Year 2011")
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    print("Group Data Month Wise for Year 2011")
    sales_year_2011_data_monthly = table_year_2011.groupby('Month').sum()['Amount']
    print(sales_year_2011_data_monthly)

    plt.bar(sales_year_2011_data_monthly.index, sales_year_2011_data_monthly.values, color="red")
    plt.xlabel("Months")
    plt.ylabel("Sales")
    plt.title("Big Mart 2011 Sales Report")
    plt.show()


"""
    3. For year 2011, plot the graph for the sales country wise
       Which country is making highest sales ?  
"""
def pie_plot():

    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print("Data for Year 2011")
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    print("Group Data Country Wise for Year 2011")
    sales_year_2011_data_country = table_year_2011.groupby('Country').sum()['Amount']
    print(sales_year_2011_data_country)

    plt.pie(sales_year_2011_data_country.values, labels=sales_year_2011_data_country.index, autopct='%1.1f%%')
    plt.show()


"""
    4. Plot Scatter Graph for the invoice amounts and see the concentration
       In which price range most of the invoices are concentrated
       for year: 2011  
"""
def scatter_plot():
    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print("Data for Year 2011")
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    print("Group Data Country Wise for Year 2011")
    sales_year_2011_data_invoice = table_year_2011.groupby('InvoiceNo').sum()['Amount']
    print(sales_year_2011_data_invoice)

    plt.scatter(sales_year_2011_data_invoice.values, sales_year_2011_data_invoice.values)
    plt.grid(True)
    plt.show()


def main():
    # sales_plot()
    # bar_plot()

    # pie_plot()
    scatter_plot()

if __name__ == '__main__':
    main()