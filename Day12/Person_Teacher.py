class Person:

    def __init__(self, name):
        self.name = name


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)


teacher = Teacher("Sara", "Python")

teacher.display()