"""
    Why Inheritance ?
    Use Case : Make My Trip

    TravelBooking
        1. FlightBooking
            from_location, to_location, date, return_date, travellers, travel_class
        2. TrainBooking
             from_location, to_location, date, travel_class
        3. BusBooking
            from_location, to_location, date
        4. CabBooking
            from_location, to_location, date, return_date, pickup_time
"""

"""
class FlightBooking:

    def __init__(self, from_location, to_location, date, return_date, travellers, travel_class):
        self.from_location = from_location
        self.to_location = to_location
        self.date = date
        self.return_date = return_date
        self.travellers = travellers
        self.travel_class = travel_class

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Flight Booked from {} to {}".format(self.from_location, self.to_location))
        print("Passengers Travelling {}".format(self.travellers))
        print("Date Of Journey {}\nReturn Journey {}\n Class:{}".format(self.date, self.return_date, self.travel_class))


class TrainBooking:

    def __init__(self, from_location, to_location, date, travel_class):
        self.from_location = from_location
        self.to_location = to_location
        self.date = date
        self.travel_class = travel_class

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Train Booked from {} to {}".format(self.from_location, self.to_location))
        print("Date Of Journey {}\n Class:{}".format(self.date, self.travel_class))



class BusBooking:

    def __init__(self, from_location, to_location, date):
        self.from_location = from_location
        self.to_location = to_location
        self.date = date

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Bus Booked from {} to {}".format(self.from_location, self.to_location))
        print("Date Of Journey {}".format(self.date))



class CabBooking:

    def __init__(self, from_location, to_location, date, pickup_time):
        self.from_location = from_location
        self.to_location = to_location
        self.date = date
        self.pickup_time = pickup_time

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Cab Booked from {} to {}".format(self.from_location, self.to_location))
        print("Date Of Journey {}\nPickup Time {}".format(self.date, self.pickup_time))


# looking above code, as a developer i have written code, which is repeated and hence a waste in time :(
# Inheritance -> Helps to Save time i.e. development time
#                Repeated Code, goes in 1 class and we will call it as Parent

"""


# Solution:
# Common Code comes to class Booking
class Booking:

    def __init__(self, from_location, to_location, date):
        print("Booking Constructor")
        self.from_location = from_location
        self.to_location = to_location
        self.date = date

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")


class FlightBooking(Booking):

    def __init__(self, from_location, to_location, date, return_date, travellers, travel_class):
        Booking.__init__(self, from_location, to_location, date) # Execute Parent's Constructor from Child
        print("FlightBooking Constructor")
        self.return_date = return_date
        self.travellers = travellers
        self.travel_class = travel_class

    def show(self):
        print("Flight Booked from {} to {}".format(self.from_location, self.to_location))
        print("Passengers Travelling {}".format(self.travellers))
        print("Date Of Journey {}\nReturn Journey {}\nClass:{}".format(self.date, self.return_date, self.travel_class))


class TrainBooking(Booking):

    def __init__(self, from_location, to_location, date, travel_class):
        Booking.__init__(self, from_location, to_location, date)
        self.travel_class = travel_class

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Train Booked from {} to {}".format(self.from_location, self.to_location))
        print("Date Of Journey {}\n Class:{}".format(self.date, self.travel_class))


class BusBooking(Booking):

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Bus Booked from {} to {}".format(self.from_location, self.to_location))
        print("Date Of Journey {}".format(self.date))


class CabBooking(Booking):

    def __init__(self, from_location, to_location, date, pickup_time):
        Booking.__init__(self, from_location, to_location, date)
        print("CabBooking Constructor")
        self.pickup_time = pickup_time

    def process_booking(self):
        print("Booking is being Processed. Please Wait..")

    def show(self):
        print("Cab Booked from {} to {}".format(self.from_location, self.to_location))
        print("Date Of Journey {}\nPickup Time {}".format(self.date, self.pickup_time))


def main():

    fRef = FlightBooking(to_location="Bangalore", from_location="Delhi", date="3rd July, 2020",
                         return_date="NA", travellers=2, travel_class="Economy")
    print(fRef.__dict__)

    fRef.process_booking()

    fRef.show()

    print()

    cRef = CabBooking(from_location="Delhi", to_location="Bangalore", date="3rd July, 2020", pickup_time="16:45")
    cRef.process_booking()
    cRef.show()

if __name__ == '__main__':
    main()
