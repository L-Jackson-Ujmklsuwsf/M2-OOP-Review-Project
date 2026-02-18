from abc import ABC, abstractmethod
import math


# Abstract Base Class

class BasicShape(ABC):
    

    def __init__(self):
        self._area = 0.0          
        self._name = ""          

    # area 
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = float(value)

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    # abstract method
    @abstractmethod
    def calc_area(self):
        pass



# Circle

class Circle(BasicShape):

    def __init__(self, x, y, r, n="Circle"):
        super().__init__()
        self._x_center = float(x)
        self._y_center = float(y)
        self._radius = float(r)
        self.name = n
        self.calc_area()

    def calc_area(self):
        self.area = math.pi * (self._radius ** 2)

    @property
    def x_center(self):
        return self._x_center

    @property
    def y_center(self):
        return self._y_center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)
        self.calc_area()   



# Rectangle

class Rectangle(BasicShape):

    def __init__(self, l, w, n="Rectangle"):
        super().__init__()
        self._length = float(l)
        self._width = float(w)
        self.name = n
        self.calc_area()

    def calc_area(self):
        self.area = self._length * self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = float(value)
        self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = float(value)
        self.calc_area()



# Square

class Square(Rectangle):

    def __init__(self, s, n="Square"):
        self._side = float(s)
        super().__init__(s, s, n)
        self.name = n  

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)
        self._length = self._side
        self._width = self._side
        self.calc_area()



# Printing of shapes:

if __name__ == "__main__":

    shapes = []

    # Two Rectangles
    shapes.append(Rectangle(10, 20, "Rectangle_1"))
    shapes.append(Rectangle(20, 30, "Rectangle_2"))

    # Two Circles
    shapes.append(Circle(0, 0, 4, "Circle_1"))
    shapes.append(Circle(5, 5, 9, "Circle_2"))

    # One Square
    shapes.append(Square(10, "Square"))

    print("--- Polymorphism check ---")
    for shape in shapes:
        print(f"{shape.name} Area = {round(shape.area, 5)}")

    print("\n--- Getter/setter check ")

    # Circle test
    circle = shapes[2]
    print(f"{circle.name} Current: {circle.radius} {round(circle.area,5)}")
    circle.radius *= 2
    print(f"{circle.name} Doubled: {circle.radius} {round(circle.area,5)}")

    # Rectangle test
    rect = shapes[0]
    print(f"{rect.name} Current: {rect.length} {rect.width} {rect.area}")
    rect.length *= 2
    rect.width *= 2
    print(f"{rect.name} Doubled: {rect.length} {rect.width} {rect.area}")

    # Square test
    square = shapes[4]
    print(f"{square.name} Current: {square.side} {square.area}")
    square.side *= 2
    print(f"{square.name} Doubled: {square.side} {square.area}")

