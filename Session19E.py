# JSON is dictionary as String Type :)

# json is a built in python module
# converts python dictionary into json
# OR reads json and converts it to python dictionary

import json

employee = {
    "name": "John",
    "phone": "+91 99999 11111",
    "salary": 30000
}

print(employee, type(employee))

# converts employee dictionary to json data i.e. string representation
json_data = json.dumps(employee)
print(json_data, type(json_data))

# convert string josn into Python Dictionary
dict_data = json.loads(json_data)
print(dict_data, type(dict_data))