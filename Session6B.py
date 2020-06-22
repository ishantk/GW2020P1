# Functions with Return
# Generally functions automatically return and we can return some data if we want


"""
def add(num1, num2):
    sum = num1 + num2
    print("sum is:", sum)
    return # This is generally the last statement in function
    # even if you do not mention lastly function will execute return automatically


add(10, 20)
add(5, -2)
print("Program Finished")

# PS: The control transfer happens automatically for us, when we execute the program
"""

def add(num1, num2):
    sum = num1 + num2
    return sum # Instead of empty returns, we can return back the data if we wish to


result = add(10, 20)
print("result is:", result)

result = add(2.2, 4.4)
print("result is:", result)

result = add(12, -19)
print("result is:", result)

# Functions can be either returning data or not returning data !!

