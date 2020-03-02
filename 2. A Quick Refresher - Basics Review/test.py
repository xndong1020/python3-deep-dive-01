class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property  # getter method to read value from field _width
    def width(self):
        return self._width

    @width.setter  # getter method to encapsulate field _width
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = value

    def area(self):
        return self.width * self.height


r1 = Rectangle(-100, 20)
