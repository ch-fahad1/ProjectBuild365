def add_student():

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    cgpa = input("Enter CGPA: ")

    with open("students.txt", "a") as file:

        file.write(f"{name},{age},{department},{cgpa}\n")

    print("Student Added Successfully.")


def view_students():

    try:
        with open("students.txt", "r") as file:

            data = file.read()

            if data:
                print(data)
            else:
                print("No Student Records.")

    except FileNotFoundError:
        print("File Does Not Exist.")


def search_student():

    name = input("Enter Student Name: ")

    found = False

    with open("students.txt", "r") as file:

        for line in file:

            if name.lower() in line.lower():

                print(line.strip())
                found = True

    if not found:
        print("Student Not Found.")


def delete_student():

    name = input("Enter Student Name to Delete: ")

    with open("students.txt", "r") as file:

        lines = file.readlines()

    with open("students.txt", "w") as file:

        deleted = False

        for line in lines:

            if name.lower() not in line.lower():
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")


while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")