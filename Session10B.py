def add(num1, num2):
    sum = num1 + num2
    print("sum of {} and {} is {}".format(num1, num2, sum))


print("add is created and its details are:", add)

# PS: If we re-create the same function again,
#     Old one will be deleted from memory and new one is in action
def add(num1, num2, num3):
    sum = num1 + num2 + num3
    print("sum of {}, {} and {} is {}".format(num1, num2, num3, sum))


print("add is re-created and its details now are:", add)


add(10, 20, 0)
add(30, 40, 0)
add(-1 ,-9, 0)