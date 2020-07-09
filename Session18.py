"""
    Modules in Python
    Any Python Program is known as MODULE :)
"""

# In a Python Module we create code:

print("1. This is Session18")
print("1. Session18 __name__ is:", __name__)

name = "John Watson"

def add(num1, num2):
    result = num1 + num2
    print("Result is:", result)


class User:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        print("User Object Constructed")

    def show(self):
        print("{} | {} | {} | {}".format(self.name, self.phone, self.email, __name__))


# We use main function to execute the code
def main():
    print("2. This is Session18")
    print("2. Session18 __name__ is:", __name__)
    add(10, 20)
    uRef = User("Fionna", "+91 98765 12345", "fionna@example.com")
    uRef.show()

if __name__ == '__main__':
    main()