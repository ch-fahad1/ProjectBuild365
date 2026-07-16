class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student = Student("Ali", 20)
student.display()