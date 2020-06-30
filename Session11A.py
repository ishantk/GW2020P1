# 1. Think of an Object
#    Shoe: name, brand_name, price, discount, color, sizes

# 2. Create its class
class Shoe:
    pass

# 3. Create Objects
shoe1 = Shoe()
shoe2 = Shoe()

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

# Above we have 2 objects in the memory as containers
# referred by shoe1 and shoe2 reference variables

# Challenges:
# 1. Different Objects need to be written data within them by developer again and again
#    i.e. for 100 objects to be created, we need to write all the attributes again and again

# 2. Different Objects may have same attributes but as a developer
# i can sometime make mistakes in writing attribute spellings or some other words

print("Shoe1 Details:")
print(shoe1.__dict__)

print("Shoe2 Details:")
print(shoe2.__dict__)

# WE NEED STANDARDIZATION TO CONSTRUCT OBJECTS
# So that we can write our algorithms to search or filter the data with ease :)

