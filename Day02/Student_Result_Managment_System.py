print("==============================")
print(" Student Result Management ")
print("==============================")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

math = float(input("Enter Math Marks: "))
english = float(input("Enter English Marks: "))
physics = float(input("Enter Physics Marks: "))
chemistry = float(input("Enter Chemistry Marks: "))
computer = float(input("Enter Computer Marks: "))

total = math + english + physics + chemistry + computer

percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"

elif percentage >= 80:
    grade = "B"

elif percentage >= 70:
    grade = "C"

elif percentage >= 60:
    grade = "D"

else:
    grade = "Fail"

print("\n==============================")
print("     Student Result Card")
print("==============================")
print("Name       :", name)
print("Roll       :", roll)
print("Math       :", math)
print("English    :", english)
print("Physics    :", physics)
print("Chemistry  :", chemistry)
print("Computer   :", computer)
print("Total      :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("==============================")