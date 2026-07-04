total_students = int(input("Enter Total Number of Students: "))

present = 0
absent = 0

for i in range(total_students):

    name = input("\nEnter Student Name: ")
    status = input("Enter Attendance (P/A): ")

    if status.upper() == "P":
        present += 1

    elif status.upper() == "A":
        absent += 1

    else:
        print("Invalid Attendance! Student ignored.")

attendance_percentage = (present / total_students) * 100

print("\n==============================")
print(" Attendance Report")
print("==============================")
print("Total Students :", total_students)
print("Present        :", present)
print("Absent         :", absent)
print("Attendance %   :", attendance_percentage, "%")
print("==============================")