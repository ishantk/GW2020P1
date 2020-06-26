# Iterating in a dictionary

state = {
    "active": 881,
    "confirmed": 3497,
    "deaths": 78,
    "recovered": 2538,
    "state": "Punjab",
}

# With Enhanced For Loop we get all the keys iterated one by one
for key in state:
    print(key)

print()

for key in state:
    value = state[key]

    print("{}\t{}".format(key, value))

print()

for value in state.values():
    print(value)

print()
# items = state.items() # List of tuples, where each tuple is a key value pair
items = list(state.items())
print(items, type(items))

for pair in items:
    # print(pair)
    print(pair[0], pair[1])

print()

for key, value in state.items():
    print(key, value)