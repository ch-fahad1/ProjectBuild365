students = []


# Function Add Student
def add_student():
    name = input("Enter Student Name: ")

    if name in students:
        print("Student already exists!")

    else:
        students.append(name)
        print("Student added successfully.")


# Function to Delete Student
def delete_student():
    name = input("Enter Student Name to Delete: ")

    if name in students:
        students.remove(name)
        print("Student deleted successfully.")

    else:
        print("Student not found.")


# Function to Search Student
def search_student():
    name = input("Enter Student Name to Search: ")

    if name in students:
        print("Student Found.")

    else:
        print("Student Not Found.")


#Function to Display Students
def display_students():

    if len(students) == 0:
        print("No students available.")

    else:
        print("\n----- Student List -----")

        for student in students:
            print(student)


while True:

    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        delete_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")