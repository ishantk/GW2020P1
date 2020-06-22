# Functions with Inputs
# Function is also known as method or procedure or routine

# Generally, function is a mathematical term
# eg: f(x) = x*x + 1, x is input and x*x + 1 is what function should do

def f(x):
    result = x*x + 1
    print("f: result with input {} is: {}".format(x, result))

def exp(x):
    result = 2 ** x
    print("exp: result with input {} is: {}".format(x, result))

def add(num1, num2):
    result = num1 + num2
    print("Addition of {} and {} is: {}".format(num1, num2, result))


f(1)
f(2)
f(3)

exp(2)
exp(3)
exp(5)

add(10, 20)
add(3, -5)
add(3.3, 2.2)

