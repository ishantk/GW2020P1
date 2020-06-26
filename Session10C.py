# Default Arguments in Functions

# def add(num1, num2, num3=0):     # OK
# def add(num1=0, num2, num3):     # ERR
# def add(num1, num2=0, num3):     # ERR
# def add(num1, num2=5, num3=0):   # OK

def add(num1=10, num2=5, num3=0):  # OK
    sum = num1 + num2 + num3
    print("sum of {}, {} and {} is {}".format(num1, num2, num3, sum))


add(10, 20)
add(30, 40)
add(-1, -9)
add()