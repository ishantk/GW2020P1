# Passing the Value Vs Passing the Reference
"""
a = 10
b = a

print("a is:", a, "and HashCode is:", id(a)) # 4297644704
print("b is:", b, "and HashCode is:", id(b)) # 4297644704

# Remember, when we create MVC they are created at different locations
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [10, 20, 30, 40, 50]

print("numbers1 is:", numbers1, "and HashCode is:", id(numbers1)) # 4330852104
print("numbers2 is:", numbers2, "and HashCode is:", id(numbers2)) # 4330971912

print("numbers1[0] is:", numbers1[0], "and HashCode is:", id(numbers1[0]))
print("numbers2[0] is:", numbers2[0], "and HashCode is:", id(numbers2[0]))
"""


# PASS BY VALUE
"""
def squareOfNumber(number):
    print("[BEFORE] number is {} and hashcode is {}".format(number, id(number))) # 11 and 4297644736
    number = number * number # we modified the number here
    print("[AFTER] number is {} and hashcode is {}".format(number, id(number)))  # 121 and 4297648256


def main():
    num = 11
    print("[BEFORE] num is {} and hashcode is {}".format(num, id(num))) # 11 and 4297644736
    squareOfNumber(num) 
    print("[AFTER] num is {} and hashcode is {}".format(num, id(num)))  # 11 and 4297644736


if __name__ == '__main__':
    main()
"""

# PASS BY REFERENCE
def squareOfNumbers(numbers):
    print("[BEFORE] numbers is {} and hashcode is {}".format(numbers, id(numbers)))

    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i] # we modified each index of numbers here

    print("[AFTER] numbers is {} and hashcode is {}".format(numbers, id(numbers)))


def main():
    nums = [10, 20, 30, 40, 50]
    # myNums = nums # Reference Copy and we did'nt create a new list
    print("[BEFORE] nums is {} and hashcode is {}".format(nums, id(nums)))
    squareOfNumbers(nums)
    print("[AFTER] nums is {} and hashcode is {}".format(nums, id(nums)))


if __name__ == '__main__':
    main()


