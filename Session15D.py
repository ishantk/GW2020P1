file = open("Session15C.py", "r")

# tell will give us position of the cursor in the file
print(file.tell())

# move the cursor 10 places
file.seek(10)

# read 15 characters from the position of cursor
data = file.read(15)
print(data)

print(file.tell())