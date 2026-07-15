class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter Name: ")
age = int(input("Enter Age: "))

student1 = Student(name, age)

student1.display()