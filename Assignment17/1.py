#class Student goes here
class Student:
    def __init__(self):
        self.score = 10

    def add_score(self):
        self.score += 10

    def decrease_score(self):
        self.score -= 10

    def __str__(self):
        return "{}".format(self.score)