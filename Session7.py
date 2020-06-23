"""
    Functions
    Value Vs Reference
    Sequence Operations
"""

# Reference Copy with Function Name
# Alias to a Function
def sayHello(name):
    print("Hello, {}".format(name))


sayHello("John")
sayHello("Fionna")

# Print the HashCode along-with Type of sayHello i.e. function
print("sayHello is:", sayHello)

# Reference Copy
hello = sayHello

print("hello is:", hello)

# hello is Alias to function sayHello
hello("Dave")
