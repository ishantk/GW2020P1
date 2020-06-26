# numbers is a list as input
# def get_max_num(numbers):

def get_max_num(*numbers):

    max = numbers[0]

    # Here we need to iterate till the end i.e. more time
    # Can we do it with some less time. Explore this !!
    for number in numbers:
        if number > max:
            max = number

    return max

# nums = [1, 2, 5, 7, 9, 11, 3]
# max_num = get_max_num(nums)
max_num = get_max_num(1, 2, 3, 7, 9, 11, 22, 12, 13)
print("Maximum number is:", max_num)