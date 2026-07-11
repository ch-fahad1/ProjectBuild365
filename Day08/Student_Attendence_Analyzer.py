
# Student Attendance Analyzer
students = []
present_students = set()
absent_students = set()


# Add Students
def add_students():

    total = int(input("Enter Total Students: "))

    for i in range(total):

        name = input(f"Enter Student {i+1} Name: ")

        students.append(name)

    print("\nStudents Added Successfully.")


# Remove Duplicate Students
def remove_duplicates():

    unique_students = list(set(students))

    students.clear()

    students.extend(unique_students)


# Mark Attendance
def mark_attendance():

    for student in students:

        status = input(f"{student} (P/A): ").upper()

        if status == "P":
            present_students.add(student)

        elif status == "A":
            absent_students.add(student)

        else:
            print("Invalid Input. Marked Absent.")
            absent_students.add(student)


# Display Report
def display_report():

    print("\n========== Attendance Report ==========")

    print("Total Students :", len(students))
    print("Present        :", len(present_students))
    print("Absent         :", len(absent_students))

    print("\nPresent Students")
    for student in present_students:
        print(student)

    print("\nAbsent Students")
    for student in absent_students:
        print(student)

    print("=======================================")


# Main Program

add_students()

remove_duplicates()

mark_attendance()

display_report()