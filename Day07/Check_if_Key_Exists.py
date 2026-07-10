student = {
    "name": "Ali",
    "age": 20,
    "cgpa": 3.8
}

key = input("Enter Key: ")

if key in student:
    print("Key Exists")
else:
    print("Key Not Found")