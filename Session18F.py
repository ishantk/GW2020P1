def area_of_circle(radius=1.0):
    area = 3.14 * radius * radius
    return area

# Reference Copy of Function
aRef = area_of_circle
print(area_of_circle)
print(aRef)

print("Area of Circle with Radius 2.5 is:", area_of_circle(2.5))
print("Area of Circle with Radius 7.15 is:", aRef(7.15))

# Lambdas in Python
# Solve Expressions as a single unit of work
lRef1 = lambda radius=1.0: 3.14 * radius * radius
print(lRef1)
print("Area of Circle with Radius 5.90 is:", lRef1(5.90))

lRef2 = lambda x, y : x**y
# lRef3 = lambda x=int(input("Enter X:")), y = int(input("Enter Y:")) : x + y

# print(lRef2(2, 5))
# print(lRef3())

lRef4 = lambda x=int(input("Enter X:")), y = int(input("Enter Y:")) : lRef1(x) + lRef2(x, y)
print(lRef4())
