class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("-----------------")


student1 = Student("Ali", 20)
student2 = Student("Sara", 21)
student3 = Student("Ahmed", 22)

student1.display()
student2.display()
student3.display()