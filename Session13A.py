# What is Inheritance?
# We link 2 Objects by a Relationship called IS-A
# We are trying to extend a type
# We generally end up in creating Parent/Child Relationship


# Rule of Inheritance -> Child can access all the
# properties in the parent if it wont have them

# In Case Child has a resource which is also in the Parent, Child will use its own resource :)

class Parent:

    # Gets executed the moment we create object in memory
    def __init__(self, fname, lname, wealth):
        print("Parent Object Constructed")
        self.fname = fname
        self.lname = lname
        self.wealth = wealth


    # Overriding
    def show(self):
        print("This is show of Parent")


class Child(Parent): # Syntax for Inheritance

    # def __init__(self):
    #     print("Child Object Constructed")

    def show(self):
        print("This is show of Child")


def main():
    # pRef = Parent()

    cRef = Child("John", "Watson", 100000)
    cRef.show()
    print(cRef.__dict__)

    print("Parent Class Dictionary")
    print(Parent.__dict__)

    print()

    print("Child Class Dictionary")
    print(Child.__dict__)

if __name__ == '__main__':
    main()
