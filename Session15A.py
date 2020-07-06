menu = {
    101: 30, # Samsosa
    201: 50, # Tikki
    301: 100,# Noodles
    401: 120,# Burger
    501: 150 # Manchurian
}


class Order:

    # This variable is created in the class and belongs to class
    # accessible by class name and is not the property of object
    order_id = 0

    def __init__(self):
        Order.order_id += 1
        self.oid = Order.order_id
        self.customer_name = input("Enter Customer Name: ")
        self.customer_phone = input("Enter Customer Phone: ")

        self.order_items = []
        choice = "yes"
        while choice == "yes":
            id = int(input("Enter Item ID: "))
            self.order_items.append("{}:{}".format(id, menu[id]))

            choice = input("Enter More (yes/no): ")

    def show_order(self):
        print("{} | {} | {}".format(self.oid, self.customer_name, self.customer_phone))
        print(self.order_items)

    def save_order(self):
        file = open("orders.csv", "a")
        data = "{},{},{},{}\n".format(self.oid, self.customer_name, self.customer_phone, self.order_items)
        file.write(data)
        file.close()
        print("Order Saved")

    # This wont take any reference to object as input
    # @staticmethod is annotation which we need to use and function wont take any self as input
    @staticmethod
    def read_orders():
        file = open("orders.csv", "r") # r -> read mode

        lines = file.readlines() # list of lines in the file

        for line in lines:
            #print(line)

            data = line.split(",")
            for i in range(0, len(data)):
                print(data[i], end=" ")

            print()


        file.close()

def main():


    choice = "yes"
    while choice == "yes":
        order = Order()
        order.show_order() # Order.show_order(order)
        order.save_order()

        choice = input("Add Next Order (yes/no): ")


    # Order.read_orders()

if __name__ == '__main__':
    main()

# Assignment:
# Convert the above Program into a Menu Driven Program
# 1. To add order
# 2. To Read Orders
# 3. To see order placed by customer with maximum price
# 4. To see maximum orders placed by customer
# 5. To see minimum orders placed by customer

# -> order_id will again become 0 if you re-run the program
#    create an algo which reads the last order_id from the file and you must use that to increment the next order id
