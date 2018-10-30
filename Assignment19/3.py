class Student:
    def __init__(self, id=0, grades=[]):
        self.id = id
        self.grades = [float(grade) for grade in grades]

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.id, self.grades)
    
    def __lt__(self, student2):
        if sum(self.grades) / len(self.grades) < sum(student2.grades) / len(student2.grades):
            return True
        else:
            return False