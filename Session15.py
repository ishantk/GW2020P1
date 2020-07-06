"""
    Persistence
        Save State of Object
        1. File Handling
        2. DataBases
            Local
            Cloud
"""

class User:

    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.phone = input("Enter Your Phone: ")
        self.email = input("Enter Your Email: ")

    def show(self):
        print("Your Details:\n{} | {} | {}".format(self.name, self.phone, self.email))


    def register_user(self):
        #file = open("data.csv", "w")    # open a file in (w) write mode, if data.csv not available, create one
        file = open("data.csv", "a")     # open a file in (a) append mode, if data.csv not available, create one
        data = "{},{},{}\n".format(self.name, self.phone, self.email)
        file.write(data)
        file.close()    # Release Memory Resources
        print("Data Saved :)")

def main():
    uRef = User()
    uRef.show()
    uRef.register_user()

if __name__ == '__main__':
    main()