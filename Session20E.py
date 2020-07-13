# We can create our own Exception Classes also
# User Defined Exceptions
class BankingError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)

class BankAccount:

    # If any user opens up a bank account
    # default balance is 10000
    def __init__(self):
        self.balance = 10000
        self.min_balance = 2000
        self.attempts = 0

    def withdraw(self, amount):
        previous_balance = self.balance
        self.balance = self.balance - amount

        if self.balance < self.min_balance:
            self.balance = previous_balance
            print("Amount {} cannot be withdrawn. Balance is Low {}".format(amount, self.balance))
            self.attempts += 1
        else:
            self.attempts = 0
            print("Amount {} withdrawn from Balance {}. New Balance is: {}".format(amount, previous_balance, self.balance))

        # we will give 3 attempts to the User
        if self.attempts == 3:
            # error = IndexError("Illegal Attempts")
            error = BankingError("Illegal Attempts")
            raise error # You can crash your program Yourself :)

def main():
    print("Banking Started")
    john = BankAccount()

    for i in range(0, 115):
        john.withdraw(3000)

    print("Banking Finished")

if __name__ == '__main__':
    main()