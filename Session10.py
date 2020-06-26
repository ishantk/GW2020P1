"""
    Dictionary
    Functions Part - II
"""

employee = {
    "eid": 101,
    "name": "John Watson",
    "designation": "Lead Engineer",
    "salary": 30000,
    "technology": "Python"
}

print(employee, type(employee), id(employee))
print("Length:", len(employee)) # as we have 5 key/value pairs
print("Max:", max(employee))    # max and min works on keys and not on values :)
print("Min:", min(employee))

# Update Data in Dictionary
employee["salary"] = 57500
print(employee)

# Later, Add an additional key anytime
employee["email"] = "john.watson@example.com"
print(employee)

del employee["eid"]
print(employee)

print(employee["name"])

# Obtain All the Keys:
# keys = employee.keys()
keys = list(employee.keys())

# Obtain All the Values:
# values = employee.values()
values = list(employee.values())

print("Keys:")
print(keys, type(keys))

print("Value:")
print(values, type(values))

# make the dictionary clear
# employee.clear()

# Do not use slicing technique as we have hash codes and not indexes
# print(employee["name":"salary"])


