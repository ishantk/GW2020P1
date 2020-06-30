"""

    OOPS in Python
    Object Oriented Programming Structure
    1. Object
    2. Class
    3. Functions in Class
    4. Standardization of Objects


    OOPS is a software design methodolgy
    We consider anything which can have data associated to it as an object

    eg:
    chair is an object
    attributes: color, make, height, width ....

    anything can be represented as an object, we must have few details known to us as its attributes

    Further, Objects have relationships

    eg: Restaurant is an Object
        attributes: name, phone, email, ratings, category etc...

        Dish is an Object
        attributes: name, category, description, price, chef

        Restaurant HAS-A Dish :)


    Object is a Multi Value Container which can hold lot of data as per our requirement

    BUT, Python gives us List, Tuple, Set and Dictionary so why do we need objects ?
    CUSTOMIZATIONS


    OOPS has 2 concepts to follow
    1. Object : Anything which has data associated to it
    2. Class  : is the code structure in which we define how the object will look like as a container
                typically, what object should have goes in the class

                attributes and functions are 2 things which we code in class and they get linked to object

"""

# Object and Dictionary are Quite Similar :)
# We already have data structures in python which can help us to store data
shoe = {
    "name": "Skateboarding Sneakers",
    "brand": "Adidas Originals",
    "price": 5999,
    "color": "black",
    "discount": 0.25
}

# Dictionary or any other data structure which is built in comes with built in functions
# and we cannot have our own functions as customizations
# Hence, we need to follow OOPS

"""
    Principle of OOPS:
    1. Think of an Object and give a Name to It.
       Object must have data associated to it which we will class as attributes
    2. Create its class.
       Standardize the structure if you wish for
    3. From the class Create the Real Object in Memory      
"""

# Use Case: Amazon Pay

# 1. Think of an Object
# Object: Beneficiary | name, ifsc, account_number, amount_to_pay, date, time
# as much as data you associate to your object more your software is refined

# 2. Create its class   # this is a type of container created by the developer and is not built in
class Beneficiary:      # class Beneficiary is representing Beneficiary Object
    pass                # we have nothing in the class

# 3. From the class Create the Real Object
ref1 = Beneficiary()    # Object Construction Statement
ref2 = Beneficiary()    # Object Construction Statement

ref3 = ref1             # Reference Copy and not an Object

print("ref1 is:", ref1, id(ref1))
print("ref2 is:", ref2, id(ref2))
print("ref3 is:", ref3, id(ref3))

# Operations On Object
# 1. Write Operation | Quite similar to dictionary (key is attribute and value is data)
ref1.name = "John"
ref1.ifsc = "SBIN0001482"
ref1.account_number = 32005678912
ref3.amount_to_pay = 3000
ref1.date = "30th June 2020"
ref3.time = "18:55"

ref2.name = "Fionna"
ref2.ifsc = "SBIN0001482"
ref2.account_number = 32005612902
ref2.amount_to_pay = 3000
ref2.date = "30th June 2020"
ref2.time = "18:55"
ref2.bank = "SBI"
ref2.email = "fionna@example.com"

# Looking above example, we can have different attributes in different objects.
# This feature may be valuable may not be as per use cases :)

# 2. Update data in Object
ref1.amount_to_pay = 7000
ref1.time = "12:55"

# 3. Delete Operation
del ref2.email

# 4. View the Data in Object
# If you wish to see the data within the object, use __dict__ which prints data of object as dictionary
print(ref1.__dict__)
print(ref2.__dict__)
print(ref3.__dict__)