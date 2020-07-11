def hello():

    print("This is Hello")

    # Nested Function: Function in a Function
    # Also Known as Local Function
    # a Function to be used by hello function only
    # memory optimization : whenever we execute hello, buy will be created only than
    def bye():
        print("This is Bye")

    print(bye)
    bye()


print(hello)
hello()