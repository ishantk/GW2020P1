# import datetime
import datetime as dt # with alias

today = dt.datetime.today()
print("Today is:", today)
print("Type of today is:", type(today))

print()

# today = str(dt.datetime.today())
# print("Today is:", today)
# print("Type of today is:", type(today))

tomorrow = dt.datetime(2020, 7, 15, 8, 18, 0)
print("Tomorrow is:", tomorrow)

# Date Time Difference
print(tomorrow - today)

# Assignment: Explore date time formatting
#             i just wish to have dd/mm/yy or hh:mm:ss data and not all together

