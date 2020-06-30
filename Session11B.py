class Shoe:

    # Constructor Function in the Class : __init__(self)
    # To standardize the Object Creation
    """
    def __init__(self): # self is a reference variable which will contain the reference to the current object
        print("init executed")
        print("self is:", self)
    """

    # This is the way we Standardize the Object
    # Constructor takes inputs
    def __init__(self, name, brand, price, discount, color, sizes):
        # LHS: self.name -> writing the data in object with attribute as name
        # RHS: and value as input in the constructor in variable name
        self.name = name
        self.brand_name = brand # Here, attribute is brand_name and value is in the variable brand copied into it :)
        self.price = price
        self.discount = discount
        self.color = color
        self.sizes = sizes


    # Any function which we create in class, will have the 1st input as by default self
    # Since, we need to work on an object
    # we need the reference to that object (hashCode)
    # and self will have it
    def show_shoe_details(self):
        print("=============================")
        print("{}\n{}\n{} {}\n{} {}".format(self.name, self.brand_name, self.price, (self.price-self.price*self.discount), self.color, self.sizes))
        print("=============================")

    def get_dicsounted_price(self):
        return self.price - self.price * self.discount




shoe1 = Shoe("Skateboarding", "Adidas Originals", 5999, 0.25, "black", [5, 6, 7, 9]) # init will be executed automatically for us
print("shoe1 is:", shoe1)
print(shoe1.__dict__)

print()

shoe2 = Shoe("AlphaBounce", "Adidas Originals", 8999, 0.40, "white", [5, 6, 7, 8, 10]) # init will be executed automatically for us
print("shoe2 is:", shoe2)
print(shoe2.__dict__)

# Now we have achieved, Standardization while creating objects in the number of attributes and naming of attributes

print()

# Later we can add or delete attributes as per our requirements
# shoe1.shoe_code = 1001
# del shoe2.color

print(shoe1.__dict__)
print(shoe2.__dict__)

shoe1.show_shoe_details()
shoe2.show_shoe_details()

print(">> {} is available at {} price".format(shoe1.name, shoe1.get_dicsounted_price()))
print(">> {} is available at {} price".format(shoe2.name, shoe2.get_dicsounted_price()))

print("Class Shoe Details")
print(Shoe.__dict__)

"""
shoe1.name = "Skateboarding"
shoe1.brandName = "Adidas Originals"
shoe1.price = 5999
shoe1.offer = 0.25
shoe1.colour = "black"
shoe1.size = (5, 6, 7, 8, 9, 10)

shoe2.name = "AlphaBounce"
shoe2.brand_name = "Adidas Originals"
shoe2.price = 8999
shoe2.discount = 0.40
shoe2.color = "white"
shoe2.size = [5, 6, 7, 8, 10]
"""