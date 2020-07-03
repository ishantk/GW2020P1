"""
    Inheritance
    Polymorphic Usage

    Use Cases
        Amazon Prime
        Ola/Uber Cab Booking

"""

# 1. Think of an Object
# Customer : name, phone, email

class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("Customer Details: {} | {} |{}".format(self.name, self.phone, self.email))


class PrimeCustomer(Customer):

    def __init__(self, customer):
        customer.prime = True
        customer.till_date = "20/02/2021"
        customer.video = True
        customer.music = True

    def upgradeToPrime(self):
        self.prime = True
        self.till_date = "20/02/2021"
        self.video = True
        self.music = True


    def showPrimeCustomer(self):
        self.showCustomer()

        prime_details = self.__dict__
        # print(prime_details)

        keys = prime_details.keys()

        for key in keys:
            print(key, prime_details[key])


def main():

    cRef1 = Customer("John", "+91 99999 11111", "john@example.com")
    # cRef1.showCustomer() # -> Translated to Customer.showCustomer(cRef)

    cRef2 = Customer("Fionna", "+91 87654 65432", "fionna@example.com")

    cRef3 = Customer("Mike", "+91 98765 12345", "mike@example.com")

    # Customer.showCustomer(cRef1)
    # Customer.showCustomer(cRef2)

    # print(cRef1.__dict__)
    # print(cRef2.__dict__)

    print()

    PrimeCustomer.upgradeToPrime(cRef2)

    primecRef1 = PrimeCustomer(cRef3)


    PrimeCustomer.showPrimeCustomer(cRef2)
    print()
    PrimeCustomer.showPrimeCustomer(cRef3)



if __name__ == '__main__':
    main()

# Assignment
# We go to a McDonald Store and ask for a Burger.
# But operator asks us to upgrade your burger to a meal
# write OOPS program using above technique as explained for mc donadls burger upgradation to meal

