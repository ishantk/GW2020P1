# Types Of Inheritance

# Single Level: 1 Parent and 1 Child
class CA:
    pass

class CB(CA):
    pass

# Multi Level: Parent Child and GrandChild
class CC(CB):
    pass

# Hierarchy   : More than 1 Child i.e. Children
class CD(CB):
    pass

# Multiple    : More than 1 Parent for 1 child
class X:
    def show(self):
        print("show of X")

class Y:
    def show(self):
        print("show of Y")

class Z(X, Y):
    pass

def main():
    zRef = Z()
    zRef.show() # Assignment: whose show should the child Z access :)


# Hybrid : any combination of above 4
