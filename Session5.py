print("WHILE LOOP")

i = 1

while i <= 10:
    print("i is:", i)
    # i += 1 # Increment i by 1
    i += 2  # Increment i by 2

# No do while loop in Python :)

print("FOR LOOP")

# for i in range(1, 11):
for i in range(1, 11, 2):
    print("i is:", i)

print("NESTED LOOP")

# Nested Loops
for i in range(1, 6): # i: 1, 2, 3, 4, 5
    print(">> i is:", i)

    for j in range(1, 4): # j: 1, 2, 3
        print(j, end=" ")

    print()

print("BREAK AND CONTINUE")

print("BREAK")
# Break and Continue
my_floor = 5
total_floors = 10
start = 1

for floor in range(start, total_floors+1):
    print("Floor#", floor)

    if floor == my_floor:
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("My Floor Arrived:", floor)
        print("~~~~~~~~~~~~~~~~~~~~~")
        break # Terminates the Loop


print("CONTINUE")
for i in range(1, 11):
    if i <= 5:
        continue    # skip the instructions below and take the loop in next iteration

    print("i is:", i)
    print("{} * {} = {}".format(5, i, (5*i)))

# Assignment:
# 1. Explore if we have labels in python with loops
# 2. Write Reverse Loops| From 10 to 1
# 3. Very closely observe how elevator works and try to write all those features in code
# 4. Write a real time use case for continue keyword

