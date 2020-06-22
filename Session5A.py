# MODEL
# Data Structure for COVID-19 Cases
# For Data Please Refer: https://api.covid19india.org/data.json

# CONTROLLER | Logical Processing on Data
#  Filtering
# 		filter by shoe size
# 		filter by shoe color[black and green]
# 	Searching
# 		To loop up for some item in a collection
# 	Sorting
# 		may be ascending or descending based on an attribute

# VIEW
# Textual input and print

state1 = {
    "active": 881,
	"confirmed": 3497,
	"deaths": 78,
	"recovered": 2538,
	"state": "Punjab",
}

state2 = {
    "active": 51922,
	"confirmed": "116752",
	"deaths": 5651,
	"recovered": 59166,
	"state": "Maharashtra",
}

state3 = {
	"active": 21993,
	"confirmed": 50193,
	"deaths": 576,
	"recovered": 27624,
	"state": "Tamil Nadu",
}

state4 = {
	"active": 27741,
	"confirmed": 47102,
	"deaths": 1904,
	"recovered": 17457,
	"state": "Delhi",
}


state5 = {
	"active": 6149,
	"confirmed": 25148,
	"deaths": 1561,
	"recovered": 17438,
	"state": "Gujarat",
}

state6 = {
	"active": 5659,
	"confirmed": 15785,
	"deaths": 488,
	"recovered": 9638,
	"state": "Uttar Pradesh",
}

state7 = {
	"active": 2721,
	"confirmed": 13626,
	"deaths": 323,
	"recovered": 10582,
	"state": "Rajasthan",
}

state8 = {
	"active": 2308,
	"confirmed": 11426,
	"deaths": 486,
	"recovered": 8632,
	"state": "Madhya Pradesh",
}

state9 = {
	"active": 4528,
	"confirmed": 7944,
	"deaths": 134,
	"recovered": 4983,
	"state": "Haryana",
}

state10 = {
	"active": 2842,
	"confirmed": 3615,
	"deaths": 115,
	"recovered": 2570,
	"state": "Karnataka",
}

# List of Dictionaries
india = [state1, state2, state3, state4, state5, state6, state7, state8, state9, state10]
print("Length of India is:", len(india))
print()


def filter():
    # 1. Filtering the data from Collection as expected by User
    filter1 = input("Please Enter 1st Filter from [active | confirmed | deaths | recovered | state]: ")
    filter2 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")

    for i in range(0, len(india)):
        print("~~~~~~~~~~~~~~~~~~")
        print("{}: {}\n{}: {}".format(filter1.upper(), india[i][filter1], filter2.upper(), india[i][filter2]))
        print("~~~~~~~~~~~~~~~~~~")
        print()


def search():
    # 2. Searching from the Data | Linear Search
    state = input("Enter the name of state to search: ")
    for i in range(0, len(india)):

        print("Matching {} with {}".format(state, india[i]["state"]))

        # if state == india[i]["state"]:
        if state.lower() == india[i]["state"].lower():
            print("State {} Found. Details are Below:".format(state))
            print(india[i])
            break

def sort():
    # 3. Sort the data | Bubble Sort
    sort_filter = input("Enter Sorting Field [active | confirmed | deaths | recovered ]: ")
    n = len(india)  # n is 10
    for i in range(0, n):  # 0, 9
        for j in range(0, n - i - 1):
            if india[j][sort_filter] > india[j + 1][sort_filter]:
                # Swap the Elements
                india[j], india[j + 1] = india[j + 1], india[j]

    print("Sorted As Per {} Cases: ".format(sort_filter))
    for i in range(0, len(india)):
        print("~~~~~~~~~~~~~~~~~~")
        print("{}: {}\n{}: {}".format("STATE", india[i]["state"], sort_filter.upper(), india[i][sort_filter]))
        print("~~~~~~~~~~~~~~~~~~")
        print()

again_choice = "yes"

while again_choice == "yes":

    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Press 1 for filtering COVID-19 Data with 2 filters")
    print("Press 2 for Search By State")
    print("Press 3 for Sorting the Cases with 1 filter")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    choice = int(input("Whats Your Choice: "))

    if choice == 1:
       filter()

    elif choice == 2:
        search()

    elif choice == 3:
        sort()

    else:
        print("Seems like you have not entered the correct choice")


    again_choice = input("Would You Like to Again Use the Program. yes to continue")

# Assignment: Linear Search goes from 0 to n-1 for n elements and for last element it will take more time as n grows
#             Explore how Binary Search Works :)

