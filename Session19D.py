# Passing Functions as Input to Other Functions

def login_with_google():
    print(">> Login with Google")

def login_with_facebook():
    print(">> Login with FaceBook")

def login_with_github():
    print(">> Login with GitHub")


# reference variable passed as input will take reference of some function
def login(login_type):
    login_type()

print("------------------------")
print("| 1. Login With Google |")
print("| 2. Login With FB     |")
print("| 3. Login With GitHub |")
print("------------------------")
choice = int(input("Enter Your Login Preference:"))

if choice == 1:
    login(login_with_google)
elif choice == 2:
    login(login_with_facebook)
elif choice == 3:
    login(login_with_github)
else:
    print("Please Enter Login Preference")

