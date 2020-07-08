"""
    Persistence
        Data in Cloud, Google Firebase
        DataBase: Firebase Firestore | NoSQL DB
        COVID ePass Use Case


        FirebaseFirestore DataBase
        it is juts like your file system
        > We have to create collections
            treat collection as a folder
        > In Collections we create documents either with name of uid (hashcode)
            Documents goes into Collections

        > Collection cannot have a collection as its child
        > Document cannot have a document as its child

        > Collection
            > Document1
            > Document1
                > Collection
                    > Document

        Firebase Firestore stores the data as dictionary list and objects

        1. Login to firebase console
        2. Create a Project | Choose a Region
        3. Configure DataBase for your Project

        Saving Data from Python Program into Firebase Firestore
        1. Create the Object To Save
        2. Install firebase-admin library
            pip install firebase-admin or from Project Interpreter in Settings
        3. Go to the Project Settings in Firebase
            > Select Service Accounts Tab

"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore        # Import firestore database from admin library

cred = credentials.Certificate("key.json")  # key.json contains all the connectivity credentials
firebase_admin.initialize_app(cred)         # creating connection to the Firebase so that we can perform any operation

print("FIREBASE INITIALIZED FOR APP")

class Pass:

    def __init__(self, name, phone, email, from_location, to_location, is_pass_granted, family_members, adrress):
        self.name = name
        self.phone = phone
        self.email = email
        self.from_location = from_location
        self.to_location = to_location
        self.is_pass_granted = is_pass_granted
        self.family_members = family_members
        self.adrress = adrress

    def show(self):
        pass

def main():

    family_members = ["John", "Jennie", "Jack"]

    address = {
        "adrs_line": "77 - B20",
        "area": "Pristine Magnum",
        "city": "Bengaluru"
    }

    pRef = Pass("Fionna", "9876512345", 'fionna@example.com', 'Ludhiana', 'Delhi', True, family_members, address)

    # To save data in firebase firestore collection, document has to be a dictionary like below :)
    # pRef_dictionary = pRef.__dict__

    # print(pRef_dictionary)

    # db is reference variable which refers to firestore database from our python program
    db = firestore.client()

    # db.collection("passes").document(pRef.phone).set(pRef_dictionary)   # Insert and Update Both :)
    # print("DATA SAVED :)")
    # print("DATA UPDATED :)")

    # db.collection("passes").document("987651234").delete()
    # print("DATA DELETED")

    # Read all the documents from Collection
    # documents = db.collection("passes").get()
    # for document in documents:
    #     print(document.id, document.to_dict())


    # Read Single Document
    document = db.collection("passes").document("9876512345").get()
    print(document.id, document.to_dict())

if __name__ == '__main__':
    main()


# Assignment:
# Create COVID-19 Curfew Pass App in Python
# A user will put up a request for issuing the pass in User App Program. include date and time also in the pass object
# A user should be able to check the status of the Pass.

# Admin App will be a separate program. Here we will list all the requests and Admin will choose whome to grant the Pass and update the status of that request

# Reference: https://epasscovid19.pais.net.in/
