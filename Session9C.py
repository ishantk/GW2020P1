app_name = "WhatsApp"
users = 1000

print(">> Welcome to", app_name)
print(">> Welcome to %s" %(app_name))

print(">> Welcome to", app_name, "We got", users, "users")
print(">> Welcome to {} We got {} users".format(app_name, users))

name = "John"
email = "john@example.com"
password = "pass123"

sql = "insert into Customer values('{}', '{}', '{}')".format(name, email, password)
print(sql)

num1 = 10
num2 = 10/3

print("Result is: {}".format(num2))

# Assignment: String Formatting
# Output: 3.3333333333333335
# Expected: 3.33