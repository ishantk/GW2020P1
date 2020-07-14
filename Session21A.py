import threading
import time

# Multi Threaded : Synchronous
#                  When multiple threads have to work on the same object, the must run synhronously
#                  i.e. one after another in parallel to the main :)

# Create Lock Object
lock = threading.Lock()

class MovieTicket:

    def __init__(self, name, seatNum, row):
        self.name = name
        self.seatNum = seatNum
        self.row = row
        self.isBooked = False

    def showMovieTicket(self):
        print("Ticket: {} | {} | {}".format(self.name, self.seatNum, self.row))


# This may take some long time
# And must be a Thread
class BookTicketTask(threading.Thread):

    def selectMovieTicket(self, ticket, email):
        self.ticket = ticket
        self.email = email


    def run(self):
        lock.acquire()

        if self.ticket.isBooked == False:
            print("Ticket Booking Started for {}".format(self.email))
            print("Movie Ticket Booked for {}".format(self.email))

            print("Movie Ticket Payment Transaction Started...")
            for i in range(0, 10):
                time.sleep(0.5) # a time delay added for processing payments
                print("Processing Payments.. {} {}".format(self.email, i))

            self.ticket.isBooked = True
            print("Email Sent to {}".format(self.email))
            self.ticket.showMovieTicket()
            print("Ticket Booking Finished for {}".format(self.email))
        else:
            print("Sorry {} ticket isnt available".format(self.email))

        lock.release()

def main():

    print("Ticket Booking App Started")

    m1 = MovieTicket("Avengers", 1, "A")
    m2 = MovieTicket("Avengers", 2, "A")
    m3 = MovieTicket("Avengers", 3, "A")
    m4 = MovieTicket("Avengers", 4, "A")
    m5 = MovieTicket("Avengers", 5, "A")

    rowA = [m1, m2, m3, m4, m5]

    task1 = BookTicketTask()
    task2 = BookTicketTask()

    # Both the users will like to book the same movie ticket :(
    task1.selectMovieTicket(rowA[2], "john@example.com")
    task2.selectMovieTicket(rowA[2], "fionna@example.com")

    task1.start()
    task2.start()


    print("Ticket Booking App Finished")

if __name__ == '__main__':
    main()