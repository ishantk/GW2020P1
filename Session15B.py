# Property of Class Vs Property of Object
class Item:

    # Property of Class
    # Can be considered as Global Variable for all the objects
    # i.e. common for all objects
    item_count = 0

    def __init__(self, item_name):
        # self.item_name and self.count : Property of Object
        self.item_name = item_name
        self.count = 0

        Item.item_count += 1


    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def show_item_count(self):
        print("Item Count is:", self.count)

    def show_items(self):
        print(Item.item_count)


def main():
    iRef1 = Item("Noodles") # iRef1: count : 0
    iRef2 = Item("Pizza")   # iRef2: count : 0
    iRef3 = Item("Burger")  # iRef3: count : 0

    iRef1.increment()       # iRef1: count : 1
    iRef1.increment()       # iRef1: count : 2

    iRef2.increment()       # iRef2: count : 1
    iRef1.decrement()       # iRef1: count : 1

    iRef2.increment()       # iRef2: count : 2

    iRef1.show_item_count() # 1
    iRef2.show_item_count() # 2
    iRef3.show_item_count() # 3

    iRef1.show_items()
    iRef2.show_items()
    iRef3.show_items()

if __name__ == '__main__':
    main()

