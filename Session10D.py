# Variable Inputs/Arguments

# args can be any name of your choice and * is mandatory in front of it
def add(*args):
    print(args, type(args))

    sum = 0

    for num in args:
        sum += num

    print("sum of {} is {}".format(args, sum))


add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, 50)
add(10, 20, -5, -9)
