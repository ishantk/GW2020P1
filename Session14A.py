"""
    Ola/Uber i.e. Cab Booking Apps

    Customer will book a Cab as a Ride by giving certain inputs
    Driver will be linked to the Ride with a Cab
    Customer has an option to select from different types of cabs

    for OLA/Uber
    i am a customer
    driver is also a Customer

    Lets write some objects for the above use case
    1. Customer: name, phone, email
    2. Driver  : extension to Customer with 2 additional attributes as below
               : licence_number, driving_experience
    3. Cab     : registration_number, base_fare
    5. OlaMini : fare
    6. OlaSedan: fare, wifi
    7. OlaBike : fare, helmet
        OlaMini, OlaSedan and OlaBike are children to Cab class

    8. RideBooking: rbn, customer, from_location, to_location, cab, driver

"""


class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show_customer(self):
        print("Name: {} | Phone: {} | Email: {}".format(self.name, self.phone, self.email))


class Driver(Customer):

    def __init__(self, name, phone, email, licence_number, driving_experience):
        Customer.__init__(self, name, phone, email)
        self.licence_number = licence_number
        self.driving_experience = driving_experience


    def show_driver(self):
        # Customer.show_customer(self)
        print("DRIVER DETAILS")
        self.show_customer()
        print("Licence: {} | Experience: {}".format(self.licence_number, self.driving_experience))


class Cab:

    def __init__(self, registration_number, base_fare):
        self.registration_number = registration_number
        self.base_fare = base_fare

    def show_cab(self):
        print("CAB DETAILS:")
        print("Reg Num: {} | Base Fare: {}".format(self.registration_number, self.base_fare))


class OlaMini(Cab):
    def __init__(self, registration_number, base_fare):
        Cab.__init__(self, registration_number, base_fare)
        self.fare = base_fare + 50

    def show(self):
        Cab.show_cab(self)
        print("Fare:", self.fare)

class OlaSedan(Cab):
    def __init__(self, registration_number, base_fare):
        Cab.__init__(self, registration_number, base_fare)
        self.fare = base_fare + 100
        self.wifi = True

    def show(self):
        Cab.show_cab(self)
        print("Fare: {} | Wifi Available: {}".format(self.fare, self.wifi))


class OlaBike(Cab):
    def __init__(self, registration_number, base_fare):
        Cab.__init__(self, registration_number, base_fare)
        self.fare = base_fare + 20
        self.helmet = True

    def show(self):
        Cab.show_cab(self)
        print("Fare: {} | Helmet Available: {}".format(self.fare, self.helmet))


class RideBooking:

    def __init__(self, customer):
        self.customer = customer
        self.rbn = 1576542

    def enter_source_destination(self):
        self.from_location = input("Enter Source Location: ")
        self.to_location = input("Enter Destination Location: ")
        print("Cab shall be booked from {} to {}".format(self.from_location, self.to_location))

    def select_cab(self):
        print("Select Cab")
        print("(Mini) | (Sedan) | (Bike)")
        choice = input("Enter The Cab of Your Choice")
        choice = choice.lower().strip()

        # Run Time Polymorphism
        # cab can be an object of OlaMini OR OlaSedan OR OlaBike
        if choice == "mini":
            self.cab = OlaMini("PB10AB1111", 100)
        elif choice == "sedan":
            self.cab = OlaSedan("PB10XY1234", 100)
        elif choice == "bike":
            self.cab = OlaBike("PB10PQ5543", 100)
        else:
            self.cab = None
            print("Please select valid Cab First")

    def attach_driver(self, driver):
        self.driver = driver

    def show_ride_booking_details(self):
        print("Ride Booking Details")
        print("Ride Booking Number:", self.rbn)
        print("Ride Booked from {} to {}".format(self.from_location, self.to_location))
        self.cab.show()
        self.driver.show_driver()
        self.customer.show_customer()


def main():
    cRef = Customer("Fionna", "+91 98765 12345", "fionna@example.com")
    dRef = Driver("John", "+91 95431 98989", "john@example.com", "DL12ABC", 3)

    print("CUSTOMER DETAILS")
    cRef.show_customer()

    print()

    dRef.show_driver()

    answer = input("Would you like to make a Booking? yes/no")
    if answer == "yes":
        rbRef = RideBooking(cRef)
        rbRef.enter_source_destination()
        rbRef.select_cab()
        rbRef.attach_driver(dRef)
        rbRef.show_ride_booking_details()

if __name__ == '__main__':
    main()

# Assignment:
# Draw the memory Object Representation for the above program

