file = open("Session15A.py", "r")

"""
line1 = file.readline()
print(line1)

line2 = file.readline() # here we will get the next line
print(line2)
"""

# Get all the content of file as lines (list of lines)
# lines = file.readlines()
# print(lines)

# Get all the content of file as string
"""
data = file.read()
print(data)
print(type(data))
"""

# To find number of functions in our program

lines = file.readlines()
count = 0
for line in lines:
    if "def" in line:
        count += 1

print("{} Functions Found".format(count))

# Source Code Analysis
# Find Number of Objects created in the Python File
# What is the class of that object
# Lastly, create a dictionary, where key is the class name and value is count of objects

