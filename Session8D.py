# Menu is a dictionary where keys are the items
# values are the prices

menu = {
    "burger": 100,
    "fries": 50,
    "noodles": 120,
    "pizza": 300,
    "samosa": 20
}

# Update Operation
menu["fries"] = 60
menu["shake"] = 150

print("Menu:")
print(menu)

# Dictionary we don't have indexes, but keys work as our customized indexes
print(menu["fries"])

item_cart = []
choice = "yes"
total = 0

while choice == "yes":

    item = input("Enter Food Item for the Cart: ")
    item_cart.append(menu[item])
    total += menu[item]

    choice = input("Would You Like to Add Another Item?  (yes/no): ")

print(item_cart)
print("Amount to Pay: ", total)

# Mini Project | Textual UI
# Open up a Food Delivery App
# Check the Menu of a Restaurant and create the same in your program
# Let the User add menu item from your menu along-with Quantity
# At the final checkout ask user for a promo code and apply the same
# In case user's bill amount is more than 500 before promo code, give him/her additional food items free

items = ["fries", "shake", "burger"]
items.extend(["nuggets", "extra fries"]) # extend will append the data in the same list

print(items)

# Explore 3 functions -> insert, remove and pop on list :)
