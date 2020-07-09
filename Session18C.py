# import all from Session 18
# from Session18 import *

# import selective
from Session18 import name
from Session18 import User

print("This is Session 18A")
print("Session18A name is:", __name__)

# PS: __name__ will be __main__ for the python module which we are executing
#     and for the imported modules, it will show the same name as that of your module name i.e. pythin file name

# Access Session18 Elements
print(name)

# add(101, 201) -> error

uRef = User("Mike", "+91 90909 10101", "mike@example.com")
uRef.show()
