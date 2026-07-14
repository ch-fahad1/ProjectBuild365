try:
    with open("student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File does not exist.")