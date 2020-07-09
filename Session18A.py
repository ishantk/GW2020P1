import Session18                # importing Session18 executes everything in Session 18 other than the main

print("This is Session 18A")
print("Session18A name is:", __name__)

# PS: __name__ will be __main__ for the python module which we are executing
#     and for the imported modules, it will show the same name as that of your module name i.e. pythin file name

# Access Session18 Elements
print(Session18.name)

Session18.add(101, 201)

uRef = Session18.User("Mike", "+91 90909 10101", "mike@example.com")
uRef.show()
