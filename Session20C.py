# In Python program is Interpreted i.e. line by line execution
# here we are not compiling the program like in other languages eg: c++, java etc..

# Any error generated shall be at run time and we call it a Run Time Error

print("Program Started")
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

result = 0

try:
    result = num1 // num2
except ZeroDivisionError as error:
    print("Some Error Occurred. Message:", error)

print("result is:", result)

print("Program Finished")

# Error at Runtime whenever comes program CRASHES
# eg num2 0, line #13 will give an Error and nothing after that will be executed
# Unfortunately Application Stopped Working
