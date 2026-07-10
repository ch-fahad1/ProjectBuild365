students = {}


#  Add Student

def add_student():

    name = input("Enter Name: ")

    if name in students:
        print("Student already exists.")
        return

    age = int(input("Enter Age: "))
    cgpa = float(input("Enter CGPA: "))

    skills = []

    total_skills = int(input("How many skills? "))

    for i in range(total_skills):
        skill = input(f"Enter Skill {i+1}: ")
        skills.append(skill)

    students[name] = {
        "age": age,
        "cgpa": cgpa,
        "skills": skills
    }

    print("Student Added Successfully.")


# Search Student

def search_student():

    name = input("Enter Student Name: ")

    if name in students:

        print("\nStudent Found")
        print("Name :", name)
        print("Age :", students[name]["age"])
        print("CGPA :", students[name]["cgpa"])
        print("Skills :", students[name]["skills"])

    else:
        print("Student Not Found.")


# Update Student

def update_student():

    name = input("Enter Student Name: ")

    if name in students:

        students[name]["age"] = int(input("Enter New Age: "))
        students[name]["cgpa"] = float(input("Enter New CGPA: "))

        print("Student Updated Successfully.")

    else:
        print("Student Not Found.")


# Delete Student

def delete_student():

    name = input("Enter Student Name: ")

    if name in students:

        del students[name]

        print("Student Deleted Successfully.")

    else:
        print("Student Not Found.")


# Display Students

def display_students():

    if len(students) == 0:
        print("No Students Found.")
        return

    print("\n========== Student Database ==========")

    for name, details in students.items():

        print("\nName :", name)
        print("Age :", details["age"])
        print("CGPA :", details["cgpa"])
        print("Skills :", end=" ")

        for skill in details["skills"]:
            print(skill, end=" ")

        print()

    print("=======================================")


# Main Menu

while True:

    print("\n====== Student Database System ======")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_students()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")