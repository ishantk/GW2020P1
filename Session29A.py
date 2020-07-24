import pandas as pd


numbers1 = [10, 20, 30, 40, 50]
numbers2 = [11, 22, 33, 44, 55]


employee1 = {"name": "John", "age": 22, "salary": 30000}
employee2 = {"name": "Fionna", "age": 24, "salary": 35000}
employee3 = {"name": "Dave", "age": 26, "salary": 55000}
employee4 = {"name": "Kim", "age": 32, "salary": 60000, "email":"kima@example.com"}


frame1 = pd.DataFrame([numbers1, numbers2])
frame2 = pd.DataFrame([employee1, employee2, employee3, employee4])

print("***Frame1***")
print(frame1)

print()

print("***Frame2***")
print(frame2)

print("===Accessing Data in DataFrame===")
print(frame1[0])        # Column wise data
print(frame2["name"])   # Column wise data

print(frame1[1][1])         # 22
print(frame2["salary"][2])  # 55000

print("===Slicing in DataFrame===")
print(frame1[0:])       # Row Wise Slicing
print(frame2[0:2])

print("===Deleting Data from DataFrame===")
# del frame1[0]   # deleting column 0
# print(frame1)

# Deleting a Row(axis=0) or Column(axis=1) -> drop function

# frame = frame1.drop(0, axis=1)
# print(frame1)    # Not Modified
# print(frame)    # Modified Result

# inplace=True -> Modifies the same frame
frame1.drop(0, axis=1, inplace=True)
print(frame1)

print("==Update Operation in DataFrame==")
frame1[1][1] = 111      # update single value
frame1[2] = 222         # Update entire column
print(frame1)

# Please explore operations on frame2 :)