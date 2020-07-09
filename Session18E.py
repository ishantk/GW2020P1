# for scientific mathematical computations
import math

class Point:

    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def show(self):
        print("Point{}: {}|{}".format(self.label, self.x, self.y))

    # Using self as the first point itself i.e. renamed self to point1
    # self will always have the HashCode of the Object which is in Use i.e. the Current Object
    def calculate_distance1(point1, point2):
        distance = math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
        print("Distance between {} and {} is: {}".format(point1.label, point2.label, distance))

    # static method is property of class
    # it will not take self as 1st input
    # @staticmethod is annotation used on top of function to make it a static method
    @staticmethod
    def calculate_distance2():
        print("calculate_distance2")

    # non static method Object's Method
    # it will first input always as self
    # i.e. which object to work on
    def calculate_distance3(self):
        print("calculate_distance3")

    @staticmethod
    def create_points_from_file():
        print("create_points")

        points = []

        file = open("points.csv", "r")
        lines = file.readlines()

        lbl = 1
        for line in lines:
            point = line.split(",")
            # read the file line by line
            # split it and convert string as int to create a Point Object
            # finally add the Same object in the list
            points.append(Point(lbl, float(point[0]), float(point[1])))
            lbl += 1

        return points

    # class method -> the 1st input like self is cls here
    # self is the reference to the current object
    # class uis the reference to the class Point
    @classmethod
    def create_points(cls):
        print("cls contains:", cls.__dict__)

        # Generally we use cls keyword to execute constructor in Class for Object Construction

        print("create_points")

        points = []

        file = open("points.csv", "r")
        lines = file.readlines()

        lbl = 1
        for line in lines:
            point = line.split(",")
            # read the file line by line
            # split it and convert string as int to create a Point Object
            # finally add the Same object in the list
            points.append(cls(lbl, float(point[0]), float(point[1])))
            lbl += 1

        return points


def main():
    p1 = Point("A", 10, 20)
    p2 = Point("B", 30, 40)

    # p1.calculate_distance(p2) # p1 goes to point1 and p2 to point 2
    Point.calculate_distance1(p1, p2)

    Point.calculate_distance2() # use class name and execute them
    Point.calculate_distance3(p1)

    points = Point.create_points_from_file()
    for point in points:
        point.show()

    print()


    print("Point Class Contains:", Point.__dict__)

    points = Point.create_points()
    for point in points:
        point.show()


if __name__ == '__main__':
    main()
