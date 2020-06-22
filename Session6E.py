a = 10  # property of main

"""
def square():
    a = 12  # property of square
    result = a * a
    print("[square] Square of {} is {}".format(a, result))
"""

def square():
    global a # please use the value/variable of main in function
    a = 12  # not property of square and we are updating it
    result = a * a
    print("[square] Square of {} is {}".format(a, result))


square()
print("This statement belongs to main")
print("a is:", a)
result = a*a
print("[main] Square of {} is {}".format(a, result))



