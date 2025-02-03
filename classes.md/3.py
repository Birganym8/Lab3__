class Shape:
    def area(self):
        print("Area:", 0)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)



rectangle = Rectangle(6, 6)
rectangle.area()  
