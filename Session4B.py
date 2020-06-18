# Bitwise and Shift Operators
# & | ^       >> <<
# Majorly used in the field of Security

num1 = 12
num2 = 4
                                    # 4 bit representation
print("binary of num1", num1, bin(num1))  # 1 1 0 0
print("binary of num2", num2, bin(num2))  # 0 1 0 0

num3 = num1 & num2
print("binary of num3", num3, bin(num3))  # 0 1 0 0

num4 = num1 | num2
print("binary of num4", num4, bin(num4))  # 1 1 0 0

num5 = num1 ^ num2
print("binary of num5", num5, bin(num5))  # 1 0 0 0

num6 = num1 >> 2
# 1 1 0 0
# 1 1 0 0 >> 2 -> _ _ 1 1 -> 0 0 1 1
print("binary of num6", num6, bin(num6))

# n >> x -> integral divide n with 2 power x
# n >> x -> integral multiplication n with 2 power x

num7 = num1 << 3
# 1 1 0 0 << 3   ->   1 1 0 0 _ _ _ -> 1 1 0 0 0 0 0
print("binary of num7", num7, bin(num7))

# Assignment: Explore what if we shift negative numbers to the right and left
#             eg: -12 >> 3 or -19 << 4

