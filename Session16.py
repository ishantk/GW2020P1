"""
    Persistence
        Introduction to MySQL DataBase
        DB Connectivity & Operation : Python and MySQL


    What is a DataBase ?
    DataBase is a collection of Tables

    What is a Table
    Its a collection of Rows & columns containing data

    Which DataBase we gonna Work ?
    1. SQL   -> MySQL from Oracle               | Structured Query Language
    2. NoSQL -> FirebaseFirestore from Google

    Installation for MySQL | XAMPP
    open localhost and go to phpMyAdmin which shows the database ui

    Databases -> create the database
    In DataBase we have tables, we will create one using SQL Language

    ORM : Object Relational Mapping
    Map Object's Attributes as Table's Column Names

    SQL Command
    create table User(
        uid int primary key auto_increment,
        name varchar(256),
        phone varchar(256),
        email varchar(256)
    )

    to add a row in table
    insert into User values(null, 'John', '+91 99999 11231', 'john@example.com')

    to update a row in table
    update User set name='Leo Watson', phone='+91 98761 12345', email='leo.watson@example.com' where uid = 3
    update User set name='Leo Watson', email='leo.watson@example.com' where uid = 3 // skip phone number

    to delete row from table
    delete from User where uid = 1


    to see all the rows
    select * from User                  // all columns
    select name, phone from User        // selective columns
    select * from User where uid = 1    // filter | >, <, =, and


    Steps to Communicate with DataBase
    1. Download the library and install it in your python project
        > Either: Settings > Project Interpreter > + to install > mysql-connector
        > OR    : pip install mysql-connector on Terminal
    2. Write SQL Statement
    3. import library in our project
    4. Create Connection with DataBase
    5. From the Connection Obtain Cursor, which performs all the DB Operations i.e. Execution of SQL Statements
    6. Execute the SQL Statement with cursor and commit :)

"""

import mysql.connector as db


class User:

    def __init__(self):
        pass

    def show(self):
        print("Your Details:\n{} | {} | {}".format(self.name, self.phone, self.email))


    def register_user(self):

        self.name = input("Enter Your Name: ")
        self.phone = input("Enter Your Phone: ")
        self.email = input("Enter Your Email: ")

        # SQL below is substituted with Object's Data
        sql = "insert into User values(null, '{}', '{}', '{}')".format(self.name, self.phone, self.email)

        # Create Connection with DataBase from Python Program
        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("Connection Created")

        # Obtain Cursor form Connection to execute SQL Statements
        cursor = connection.cursor()

        # Execution of SQL Statement
        cursor.execute(sql)
        connection.commit() # to ensure your SQL Statement gets executed over the connection

        print("User Saved in DataBase")

    def update_user(self):

        self.uid = int(input("Enter User's UID: "))
        self.name = input("Enter Your Name: ")
        self.phone = input("Enter Your Phone: ")
        self.email = input("Enter Your Email: ")

        # SQL below is substituted with Object's Data
        sql = "update User set name='{}', phone='{}', email='{}' where uid = {}".format(self.name, self.phone, self.email, self.uid)

        # Create Connection with DataBase from Python Program
        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("Connection Created")

        # Obtain Cursor form Connection to execute SQL Statements
        cursor = connection.cursor()

        # Execution of SQL Statement
        cursor.execute(sql)
        connection.commit() # to ensure your SQL Statement gets executed over the connection

        print("User Updated in DataBase")

    def delete_user(self):

        self.uid = int(input("Enter User's UID: "))

        # SQL below is substituted with Object's Data
        sql = "delete from User where uid = {}".format(self.uid)

        # Create Connection with DataBase from Python Program
        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("Connection Created")

        # Obtain Cursor form Connection to execute SQL Statements
        cursor = connection.cursor()

        # Execution of SQL Statement
        cursor.execute(sql)
        connection.commit() # to ensure your SQL Statement gets executed over the connection

        print("User Deleted from DataBase")


    def fetch_all_users(self):

        # SQL below is substituted with Object's Data
        sql = "select * from User"

        # Create Connection with DataBase from Python Program
        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("Connection Created")

        # Obtain Cursor form Connection to execute SQL Statements
        cursor = connection.cursor()

        # Execution of SQL Statement
        cursor.execute(sql)
        rows = cursor.fetchall()  # Give me all the rows | Rows is a list of Tuples, where every tuple has data in column
        print("All Users:")
        for row in rows:
            # print(row)
            print(row[0], row[1], row[2], row[3])

    def fetch_user(self, uid):

        # SQL below is substituted with Object's Data
        sql = "select * from User where uid = {}".format(uid)

        # Create Connection with DataBase from Python Program
        connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        print("Connection Created")

        # Obtain Cursor form Connection to execute SQL Statements
        cursor = connection.cursor()

        # Execution of SQL Statement
        cursor.execute(sql)
        rows = cursor.fetchall()  # Give me all the rows | Rows is a list of Tuples, where every tuple has data in column
        print("All Users:")
        for row in rows:
            # print(row)
            print(row[0], row[1], row[2], row[3])


def main():
    uRef = User()

    # uRef.show()
    # choice = input("Would you like to Save the User(yes/no) ?")
    # if choice == "yes":
    #     uRef.register_user()

    # uRef.register_user()
    # uRef.update_user()

    # uRef.delete_user()

    # uRef.fetch_all_users()

    uRef.fetch_user(4)

    print("Thank You for Using the Software")

if __name__ == '__main__':
    main()


# Assignment: Save the data for Curfew ePass: Refer link https://epasscovid19.pais.net.in/