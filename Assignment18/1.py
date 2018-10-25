#class Pair goes here
class Pair:
    def __init__(self, v1=0, v2=0):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.v1, self.v2)

    def __add__(self, class2):
        return Pair(self.v1 + class2.v1, self.v2 + class2.v2)