import math
class Circle:
    def __init__(self, radius=0.0):
        self.__radius = float(radius)

    def get_radius(self):
        return self.__radius    
    
    def set_radius(self, userinput):
        self.__radius = userinput

    def __str__(self):
        return "Area: {0:.2f}\nPerimeter: {1:.2f}".format(math.pi * self.__radius ** 2, 2 * math.pi * self.__radius)