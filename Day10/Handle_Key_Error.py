student = {
    "name": "Ali",
    "age": 20,
    "cgpa": 3.7
}

try:
    key = input("Enter Key: ")

    print(student[key])

except KeyError:
    print("Error: Key not found.")