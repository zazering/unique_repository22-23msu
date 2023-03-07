class Person:
    marks = []
    num_of_project = 0

    def __init__(self, name, sex, age, num_of_projects):
        self.num_of_subjects = num_of_projects
        self.name = name
        self.sex = sex
        self.age = age
        if 1 <= num_of_projects <= 10:
            self.num_of_projects = num_of_projects
        else:
            raise ValueError("Wrong num of subjects")

    def __str__(self):
        return f"My name is {self.name}. I'm {self.age}. I have {self.num_of_projects} subjects"

    def setMarks(self, marks):
        if type(marks) == str:
            marks = " ".join(marks.split(";"))
            marks = [int(i) for i in marks.split()]
        if not len(marks) == self.num_of_subjects:
            raise ValueError("wrong num of marks")
        for mark in marks:
            if not 0 <= mark <= 10:
                raise ValueError("wrong num of mark")

        self.marks = marks


def main():
    a = Person("Masha", 0, 12, 3)
    a.setMarks([-1, 2, 3])
