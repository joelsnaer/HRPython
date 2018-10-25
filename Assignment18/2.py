#class MyString goes here
class MyString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return "{}".format(self.string)

    def __sub__(self, class2):
        return len(self.string) - len(class2.string)
        
    def __gt__(self, class2):
        return len(self.string) > len(class2.string)