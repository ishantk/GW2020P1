# Conditional Operators
# ==, !=, >, <, >=, <=

# Logical Operators
# and, or

# Membership Operators
# is, is not

cabFare = 100
wallet = 70

print("Can i Book the Cab: ", (cabFare <= wallet))

username = "john.watson@example.com"
password = "password123"

print("User Authentication 1: ", (username == "john@example.com"))
print("User Authentication 2: ", (password == "password123"))

print("User Authentication for Login: ", (username == "john@example.com") and (password == "password123"))

otp = 3027
user_otp = int(input("Enter The OTP: "))

print("OTP Matched:", (otp == user_otp))

# Boolean or bool
isInternetOn = False
print("Can i Login? ", isInternetOn, type(isInternetOn))


print("===Membership===")
a = 10
print(a is 10)
print(a == 10)

name = "Fionna"
print(name == "Fionna")
print(name is "Fionna")

print(name is not "John")
print(name != "John")

# as of now is and == are performing same
# Assignment: Explore the difference between is and ==
#             Hint: HashCodes :)
