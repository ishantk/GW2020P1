"""
    Sequences in Continuation
"""

numbers = [10, 20, 30, 40, 50]
print(">> numbers are:", numbers, id(numbers))

# Concatenation Operation means we need to save new result in another variable
# more_numbers = numbers + [11, 22, 33, 44, 55]
# print(">> more_numbers are:", more_numbers, id(more_numbers))

numbers = numbers + [11, 22, 33, 44, 55]

print(">> numbers now are:", numbers, id(numbers))