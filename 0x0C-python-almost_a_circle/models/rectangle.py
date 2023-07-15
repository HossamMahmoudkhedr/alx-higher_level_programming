#!/usr/bin/python3
""" Rectangle class """
from base import Base


class Rectangle(Base):
    '''
        Defining the Rectangle class
        Inherits from:
            Base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    def Validation(self, number, name):
        if not isinstance(number, int):
            raise TypeError("{} must be an integer".format(name))

        if name == 'width' or name == 'height':
            if number <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if number < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.Validation(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.Validation(height, "height")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.Validation(x, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.Validation(y, "y")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for col in range(self.__height):
            for row in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x, self.__y, self.__width, self.__height)



r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)

r2 = Rectangle(5, 5, 1)
print(r2)