"""
    Generator in Python
    yield keyword
"""

def hello():
    print(">> This is hello")
    return "Hello"
    return "Heya" # will not be executed


print(hello)
result = hello()
print(result)


def hello_again():
    print(">> This is hello again")
    yield "Hello"
    yield "Hi"
    yield "Heya"
    yield "Hola"

print(hello_again)
result = hello_again() # returns back a generator object upon its execution
print(result)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result)) # StopIteration Error