import random

# from 0 to 1000 with step of 1
# we can get any random number
otp = random.randrange(10000)
print("1. OTP is:", otp)

otp = random.randrange(2000, 4000)
print("2. OTP is:", otp)

otp = random.randrange(2000, 4000, 10)
print("3. OTP is:", otp)

# we cannot give a step here
otp = random.randint(1000, 9000)
print("4. OTP is:", otp)

# Assignment: Create a Random Function using some Algorithm Yourself :)
# def my_random_generator(from, to, step):
#     pass