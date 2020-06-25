# Built In Functions on String

# RULE: Strings are IMMUTBALE. Any Manipulation Operations generates a new String

name = "Fionna Flynn"
upper_name = name.upper()   # lower()

print("Name is:", name)
print("Name in Upper Case is:", upper_name)

author_name = "john watson"
cap_author_name = author_name.capitalize()
print("Author is:", author_name)
print("Author Name Capitalised is:", cap_author_name)
        #0123456........
names = "John, Jennie, Jim, Jack, Joe, Kim, Sim"
print(names[0])                 # J
print(names[len(names)-1])      # e

idx = names.index('h')
print("idx of h is:", idx)      # 2

idx = names.index("Jennie")
print("idx of Jennie is:", idx) # 6

splitted_names = names.split(",")
print(splitted_names, type(splitted_names))

for name in splitted_names:
    print(name.strip())


# replaced_names = names.replace('J', 'K')
replaced_names = names.replace('im', 'oa')
print(replaced_names)

j_char_count = names.count('J', 0, len(names))
print("j_char_count is:", j_char_count)

# API: Application Programming Interfaces

quote = "Live Life King Size"
for i in range(0, len(quote)):
    print(quote[i], end=' ')

print()

for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=' ')

print()

salutation = "Mr."
fname = "George"
lname = "Watson"

# Concatenation
full_name = salutation + fname + " " +lname
print(full_name)

number = "100"
print(number, type(number))
print(number.isdigit()) # explore all these is functions

file_names = ["song1.mp3", "abc.mp4", "xyz.mp3", "pqr.docx", "jkl.pdf"]
for name in file_names:
    if name.endswith(".mp3"): # startsWith
        print(">> You Can Play this song:", name)


