"""
   Map, Filter and Reduce
   Using Built In Modules in Python

"""

def discount(amount):
    return amount - amount*0.20


product_prices = [1234, 2045, 2345, 3467, 9091]

lRef1 = lambda amount: amount - amount*0.20

for price in product_prices:
    print(lRef1(price))

# map is a built in function in python
# map maps the data with the lambda or function

# result = map(discount, product_prices) # execution where we get map object returned back
result = map(lRef1, product_prices)
print(result, type(result))
print(list(result))

print(list(map(lambda num: num/2, product_prices)))

# numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers = list(range(10, 21))
print(numbers)

l1 = lambda num: num%2 == 0    # Even Number
l2 = lambda num: num%2 != 0    # Odd Number

print(list(map(l1, numbers)))
print(list(map(l2, numbers)))

print(list(filter(l1, numbers)))
print(list(filter(l2, numbers)))

# filter is used to extract data from the list based on boolean evaluation

numbers2 = list(range(20, 31))

l3 = lambda X, Y: X + Y

print(l3(numbers, numbers2))

# reduce function can be used to reduce the list by some computation to a single number as a result
from functools import reduce

nums = [10, 20, 30, 40, 50]
result = reduce(l3, nums)
print(result)


# Generally Looping Operations with Computations can be managed with
# Map       |   Apply the same logic on all elements of list
# Filter    |   Apply the same logic on all elements and extract selective elements
# Reduce    |   Apply computation on all elements to get back a single result value

# explore above functions in : tuple, set and dictionary :)
