"""
    Misc Concepts in Python
"""

# object is a Built in Class in Python
# by default, every class is inherited by object class
# object is a parent class to every class

# class Point(object):
#     pass
# These are both same meaning : object will become the parent automatically
# class Point:
#     pass


class Product:  # by default child of object

    def __init__(self, name, brand, price):
        self.name = name
        self._brand = brand     # protected variable: let it be accessed only by child classes
        self.__price = price    # private variable  : must not be accessed

    # if we make anything in our class as private
    # Name Mangling comes into action i.e. name will be modified
    #_classname will be added in front of name -> _Product__showProduct()
    def __showProduct(self):
        print("Product Details: {} | {} | {}".format(self.name, self._brand, self.__price))

    # __somename__ methods in python are called MAGICAL METHODS
    
    # Override the string function so that we can return some meaningful data whenever we print reference variable
    def __str__(self):
        return "{} | {} | {}".format(self.name, self._brand, self.__price)


def main():
    pRef = Product("iPhone", "Apple", 60000)
    # pRef.__showProduct()  error # This is error as it was marked private and we are trying to accesss it

    print(Product.__dict__)
    pRef._Product__showProduct()    #indirect access


    print(pRef.__dict__)
    print(pRef._brand)
    # print(pRef.__price) error
    print(pRef._Product__price)


    print(pRef) # automatically executes __str__()
    print(pRef.__str__())
    string_data = str(pRef)
    print(string_data)


if __name__ == '__main__':
    main()



