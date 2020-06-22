"""
    Functions in Python

    We can have a case where out piece of logic needs to be executed again and again
    Use Case:
        Taxes on products needs to be computed at many places in an e-commerce platform
        1. When we show the product Prices
        2. When we Show th Cart Value
        3. When we Checkout
        4. When we create an invoice/bill

    Functions are small code snippets with a name gaven so as to modularize the program

"""
# Create a Function by using keyword def
# Give any name to your function eg: add here and put () alongwith it
# Whatever we write in the function in known as its definition
def add():
    number1 = int(input("Enter Number 1: "))
    number2 = int(input("Enter Number 2: "))

    sum = number1 + number2
    print(">> SUM is {}".format(sum))


# Execution of Function
add()
add()