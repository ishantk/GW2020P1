"""

    OOPS
    HAS-A RELATIONSHIP

    How 2 Objects are related to each other

    1 Restaurant Has 1 Menu | 1 to 1
    1 Menu Has Many Dishes  | 1 to *

    A Food Delivery App Has Many Restaurants

"""

# 1. Think of Object
# Restaurant | name, categories, area, feedback, time_to_deliver, price_per_person, menu (has-a)
# Menu       | name, dishes (has-a), count
# Dish       | name, description, price, discount

# 2. Write Classes for Objects
# Here a small tip is to begin with the class for object who is not having any other relation

class Dish:

    def __init__(self, name, description, price, discount):
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount

    def show_dish(self):
        print("========DISH=========")
        print("{}\n{}\n{} | {}".format(self.name, self.description, self.price, (self.price-self.discount*self.price)))
        print("====================")
        print()


class Menu:

    def __init__(self, name, dishes, count): # dishes is a List
        self.name = name
        self.dishes = dishes                 # HAS-A Relationship Fulfillment
        self.count = count

    def show_menu(self):
        print("~~~~~~~~MENU~~~~~~~~")

        print("{} [{}]".format(self.name, self.count))

        print("{} Dishes".format(self.name))

        for dish in self.dishes:
            dish.show_dish()

        print("~~~~~~~~~~~~~~~~~~~~")


class Restaurant:

    def __init__(self, name, categories, area, feedback, time_to_deliver, price_per_person, menu):
        self.name = name
        self.categories = categories
        self.area = area
        self.feedback = feedback
        self.time_to_deliver = time_to_deliver
        self.price_per_person = price_per_person
        self.menu = menu                # HAS-A Relationship Fulfillment

    def show_restaurant(self):
        print("*******Restaurant {}*******".format(self.name))
        print(self.categories)
        print("{} | {}\n{} | {}".format(self.area, self.feedback, self.time_to_deliver, self.price_per_person))

        print("{} Menu".format(self.name))

        self.menu.show_menu()
        print("***************************")


# Cart: dishes, dish_count, item_count, total_value
#       paneer [2], dal[1] | dish_count: 2, item_count: 3

class Cart:
    pass



def main():

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Welcome to Our Food Delivery App")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


    """
    dish1 = Dish("Plain Channa Bhatura", "Exotic Flavour From Delhi", 170, 0.5)
    dish2 = Dish("Paneer Channa Bhatura", "Exotic Flavour From Delhi", 240, 0.5)
    dish3 = Dish("Lassi", "Exotic Flavour From Delhi", 80, 0.4)
    dish4 = Dish("Channa", "Exotic Flavour From Delhi", 50, 0.3)

    dishes = [dish1, dish2, dish3, dish4]

    menu = Menu("Pure Veg", dishes, len(dishes))

    restaurant = Restaurant("Delhi Riyasat", ["North Indian", "Fast Food", "Snacks"], "Civil Lines", 4.5, 39, 150, menu)

    restaurant.show_restaurant()
    """

    restaurant = Restaurant(
        name="Delhi Riyasat",
        categories=["North Indian", "Fast Food", "Snacks"],
        area="Civil Lines",
        feedback=4.5,
        time_to_deliver=39,
        price_per_person=150,
        menu=Menu(
            name="Pure Veg",
            dishes=[
                Dish("Plain Channa Bhatura", "Exotic Flavour From Delhi", 170, 0.5),
                Dish("Paneer Channa Bhatura", "Exotic Flavour From Delhi", 240, 0.5),
                Dish("Lassi", "Exotic Flavour From Delhi", 80, 0.4),
                Dish("Channa", "Exotic Flavour From Delhi", 50, 0.3)
            ],
            count=4)
    )

    restaurant.show_restaurant()

    restaurant_dictionary = {
        "name": "Delhi Riyasat",
        "categories": ["North Indian", "Fast Food", "Snacks"],
        "area": "Civil Lines",
        "feedback": 4.5,
        "time_to_deliver": 39,
        "price_per_person": 150,
        "menu":{
            "name": "Pure Veg",
            "dishes":[
                {"name":"Plain Channa Bhatura", "description":"Exotic Flavour From Delhi", "price":170, "discount":0.5},
                {"name": "Paneer Channa Bhatura", "description": "Exotic Flavour From Delhi", "price": 240,
                 "discount": 0.5},
                {"name": "Lassia", "description": "Exotic Flavour From Delhi", "price": 80,
                 "discount": 0.4},
                {"name": "Channa", "description": "Exotic Flavour From Delhi", "price": 50,
                 "discount": 0.3},
            ],
            "count":4}
    }

    print(restaurant_dictionary)

    # Assignment:
    # Create at-least 10 restaurant objects
    # Implement: Search, Sort and Filter as per your choice on few attributes
    # eg: sort the restaurants as per price_per_person
    #     filter all the restaurants which are having category as Snack
    #     Search a restaurant by name
    # Take Reference from COVID-19 Case Study


if __name__ == '__main__':
    main()
