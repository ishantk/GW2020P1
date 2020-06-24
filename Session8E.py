# Conversions
numbers1 = (10, 20, 30, 40, 50, 20, 10)
print(numbers1, type(numbers1), id(numbers1))

print()

# Converting Tuple into list: Creating a new list out of tuple at new memory location
numbers2 = list(numbers1)
print(numbers2, type(numbers2), id(numbers2))

print()

numbers3 = set(numbers2)
print(numbers3, type(numbers3), id(numbers3))

# Below is Error: as dictionary works on key value pair
# numbers4 = dict(numbers3)
# print(numbers4, type(numbers4), id(numbers4))

# Explore, where dict() function will be used and how ?

print()
print(numbers1)
print(numbers1[::-1]) # Reverse the List
