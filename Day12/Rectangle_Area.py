class Shape:

    def area(self):
        print("Area Formula")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)


rectangle = Rectangle(10, 5)

rectangle.area()