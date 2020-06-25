name = "John Watson"
print(name, type(name), id(name))

another_name = "John Watson"
print(another_name, type(another_name), id(another_name))

# name and another_name are reference variables which shall point to Data

print("Length of name is:", len(name))
print("Minimum of name is:", min(name))
print("Maximum of name is:", max(name))

# phone = input("Enter Your Phone Number:")
# print("Thank You for confirming your Phone:", phone, len(phone))

# Indexing
print(name[1])

print(name[len(name)-1]) # last Index
print(name[-2]) # second last Index

print(name[::-1])

# Slicing
phone = "+91 99155 71177"
print(phone[4:9])
print(phone[10:len(phone)])

print(phone[4:])
print(phone[:4])

# Membership Testing
email = input("Enter Your Email: ")
print("You Entered:", email)

if "@" in email and "." in email:
    print("Thank You for Subscribing to Us")
else:
    print("Please provide a Valid Email for Subscribing to Us")

# Replication
print(phone*2)
