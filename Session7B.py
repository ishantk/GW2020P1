"""
    Sequences in Python
    Data in a Multi Value Container | same (homo) or different (hetro) type

    1. tuple
    2. list
    3. set
    4. dictionary
    5. string

    In Computer Science, we call them as Data Structures also

    some works on indexing others on hashing
    tuple, list and string -> indexing
    set and dictionary     -> hashing

    Operations:
    1. Concatenation
    2. Repetition
    3. Membership testing
    4. Indexing
    5. Slicing


"""

students = ("john", "jennie", "jim", "jack", "joe")
print("students:", students)
print("type of students:", type(students))

print()

# 1. Concatenation | Generates a new tuple
moreStudents = students + ("fionna", "dave", "kia")
print("moreStudents:", moreStudents)
print("students now is:", students) # IMMUTABLE
print("type of moreStudents:", type(moreStudents))

print()

# 2. Repetition | Generates a new tuple
repeatedStudents = students * 3
print("repeatedStudents:", repeatedStudents)
print("students now is:", students) # IMMUTABLE

print()

# 3.Membership testing
print("john" in students)
print("lee" not in students)

print()

# 4.Indexing
print(students[0])
print(students[len(students)-1]) # last index i.e. joe
print(students[-1]) # last index i.e. joe
print(students[-5]) # first index john
# print(students[-6]) # Error

print()

# 5.Slicing
print(students[0:3]) # 0, 1 and 2 | 0 inclusive and less than 3 i.e. 2, 3 is not inclusive
print(students[2:]) # from 2 till end
# Here, try out negative indexes on slicing


print()

# Loops on Sequences
for i in range(0, len(students)):
    print(students[i])

print()

# Enhanced For Loop on Sequences | for-each loop
for name in students:
    print(name)

# Assignment:
#   Implement all above features on other sequences :)
#   Also for Loop and Enhanced Loop
