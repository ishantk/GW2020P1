ids = {"john.w", "fionna", "dave.h", "kia", "ana"}
print(ids, type(ids), id(ids))
# Above Set works on Hashing
# Hence we cannot apply indexing or Slicing on it

# So, we need to iterate in the set to access elements
# for i in range(0, len(ids)):
#     print(ids[i])   # Error

# Set Supports Enhanced For Loop

for id in ids:
    print(id)

print("~~~~~~~")
print(len(ids))

# If we have data as Strings, max min works with ASCII Code comparison but only for the 1st character
print(max(ids))
print(min(ids))

# Reference to ASCII CODES
# http://www.asciitable.com/