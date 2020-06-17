# Multi Value Container
# Dictionary In Python also known as Map
# Stores the Data as key value pair

restaurant = {
    "name": "Gopal Sweets",
    "reviews": 4.3,
    "categories": ["Mithai", "Indian", "Bakery", "Fast Food"],
    "time_to_deliver": 41,
    "promo_code": "CRAVINGS",
    1: "1356"
}

print(restaurant)
print(type(restaurant))
print(len(restaurant)) # is number of keys in dictionary

# We can have any type of key or any type of value
# Homo or Hetro

dish1 = {
    "name": "Gujiya",
    "price": 125,
}

dish2 = {
    "name": "Khoya Burfi",
    "price": 150,
}

dish3 = {
    "name": "Milk Cake",
    "price": 200,
}

# List of Dictionaries
dishes = [dish1, dish2, dish3]

# Adding Key Later and its a key containing list of dictionaries
restaurant["dishes"] = dishes

print(restaurant)

# Assignment : Replicate any of the amazon web page with products
