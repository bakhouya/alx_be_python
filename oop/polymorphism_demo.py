import math

# ================================================================================================
# her I have created a class Shape this class has a method area() which is not implemented
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method.")
# ================================================================================================

# ================================================================================================
# here I have created a class Rectangle which inherits from shape and implements the area() method
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
# ================================================================================================


# ================================================================================================
# here I have created a class Circle which inherits from shape and implements the area() method
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
# ================================================================================================