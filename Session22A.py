import datetime as dt

class Fee:

    def __init__(self, rollNum=0, amount=0):
        self.rollNum = rollNum
        self.amount = amount
        self.datetime = dt.datetime.today()


    def show_fee(self):
        print("{} | {} | {}".format(self.rollNum, self.amount, self.datetime))


    # def add(self, fee):
    def __add__(self, fee): # Operator Overloading -> + operator will not be used to execute this function
        temp = Fee()
        temp.amount = self.amount + fee.amount
        return temp

    # def __mul__(self, other):
    # def __sub__(self, other):
    # def __divmod__(self, other):

    # many others to explore for operator overloading

    def __copy__(self):
        print("DEEP COPY")
        temp = Fee(self.rollNum, self.amount)
        temp.datetime = self.datetime
        return temp

def main():

    fRef1 = Fee(101, 2000)
    fRef2 = Fee(201, 2400)
    fRef3 = Fee(301, 3100)


    # totalFeeRef = fRef1.add(fRef2).add(fRef3)
    # print(totalFeeRef.amount)

    # applied + operator on Objects where the natural meaning of + operator is to add numbers
    totalFeeRef = fRef1 + fRef2 + fRef3     # fRef1.__add__(fRef2).__add__(fRef3)
    print(totalFeeRef.amount)

    # fRef1 and my_fee both points to the same memory location
    # my_fee = fRef1 # Shallow Copy as we juts make 2 references pointing to the same object with same data

    my_fee = fRef1.__copy__() # Deep Copy Operation where, 2 References points to 2 different objects and may or may not share the same data later but initially it would be same
    print(fRef1)
    print(my_fee)

    print(fRef1.__dict__)
    print(my_fee.__dict__)


if __name__ == '__main__':
    main()