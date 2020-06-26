def get_max_number(data, length):

    if length == 1:
        return data[0] # for elements in list with length 1, that element itslef is the max which is 0 index
    else:
        num = get_max_number(data, length-1)

    if num > data[length-1]:
        return num
    else:
        return data[length-1]


numbers = [10, 20, 30]
max = get_max_number(numbers, 3)
print("max number is:", max)


# Assignments
# print binary representation of a decimal number using function and recursion

# 12 -> 1 1 0 0
# 9  -> 1 0 0 1

# Find the state with maximum and minimum cases in COVID-19 Case Study :)

"""
def f1():
    f1()    # function calling itself again: Direct Recursion

def f2():
    f3()    # Indirect Recursion

def f3():
    f2()    # Indirect Recursion
    
def f4():
    .
    ...
    .....
    f4()    # Tail Recursion, when last execution is function call
"""