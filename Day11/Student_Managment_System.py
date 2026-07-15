class Student:

    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display(self):
        print("\n------------------------")
        print("Name :", self.name)
        print("Age :", self.age)
        print("CGPA :", self.cgpa)
        print("------------------------")


students = []


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    cgpa = float(input("Enter CGPA: "))

    student = Student(name, age, cgpa)

    students.append(student)

    print("Student Added Successfully.")


def display_students():

    if len(students) == 0:
        print("No Students Found.")
        return

    for student in students:
        student.display()


def search_student():

    name = input("Enter Student Name: ")

    for student in students:

        if student.name.lower() == name.lower():

            student.display()

            return

    print("Student Not Found.")


def delete_student():

    name = input("Enter Student Name: ")

    for student in students:

        if student.name.lower() == name.lower():

            students.remove(student)

            print("Student Deleted Successfully.")

            return

    print("Student Not Found.")


def update_student():

    name = input("Enter Student Name: ")

    for student in students:

        if student.name.lower() == name.lower():

            student.age = int(input("Enter New Age: "))
            student.cgpa = float(input("Enter New CGPA: "))

            print("Student Updated Successfully.")

            return

    print("Student Not Found.")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        display_students()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")