# Class Rectangle goes here
class Rectangle:
    def __init__(self, length=0, width=0):
        self.__length = 0
        self.__width = 0
        if length > 0:
            self.__length = length
        if width > 0:
            self.__width = width


    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2*(self.__length + self.__width)
        
    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)

    def __eq__(self, class2):
        if self.__width == class2.__width and self.__length == class2.__length:
            return True
        elif self.__width == class2.__length and self.__length == class2.__width:
            return True
        else:
            return False
    def __repr__(self):
        return "Rectangle({},{})".format(self.__length, self.__width)