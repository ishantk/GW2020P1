restaurat1 = {
    "title": "Nik Bakers",
    "timeToDeliver": 60
}

restaurat2 = {
    "title": "Just Laid Eggs",
    "timeToDeliver": 50
}

restaurat3 = {
    "title": "Gopal Sweets",
    "timeToDeliver": 120
}

restaurat4 = {
    "title": "Table By Basant",
    "timeToDeliver": 30
}


restaurat5 = {
    "title": "Ice Cream Studio",
    "timeToDeliver": 45
}

# List of Dictionaries
# Indexing:      0             1            2           3           4
restaurants = [restaurat1, restaurat2, restaurat3, restaurat4, restaurat5]
print("Restaurants: ")
# print(restaurants)

"""
print(restaurants[0])
print(restaurants[1])
print(restaurants[2])
print(restaurants[3])
print(restaurants[4])
"""

# here i value will vary from 0 to 4 i.e. i will become 0, 1, 2, 3, and 4
for i in range(0, 5):
    # print(restaurants[i])
    print(restaurants[i]['title'], "\t", restaurants[i]['timeToDeliver'])
    print("~~~~~~~~~~~~~~~~~~~~~")

print()

# Filter restaurants on the basis of time < 50 mins
print("Resturants Delivering in less than 50 mins")
for i in range(0, 5):

    if restaurants[i]['timeToDeliver'] <= 50:
        print(restaurants[i]['title'], "\t", restaurants[i]['timeToDeliver'])
        print("~~~~~~~~~~~~~~~~~~~~~")

"""
Assignment : COVID 19 Case Study | https://api.covid19india.org/data.json
    covid19_pujab = {
        "active": 881,
        "confirmed": 3497,
        "deaths": 78,
        "deltaconfirmed": "0",
        "deltadeaths": "0",
        "deltarecovered": "0",
        "lastupdatedtime": "17/06/2020 19:35:50",
        "migratedother": "0",
        "recovered": 2538,
        "state": "Punjab",
        "statecode": "PB",
        "statenotes": ""
    }
    
    Evaluate and give the results:
    1. State with max deaths cases
    2. State with max active cases
    3. State with max confirmed cases
    4. State with max recovered cases

"""