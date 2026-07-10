students = {
    "Student1": {
        "name": "Ali",
        "age": 20
    },

    "Student2": {
        "name": "Ahmed",
        "age": 21
    },

    "Student3": {
        "name": "Sara",
        "age": 22
    },

    "Student4": {
        "name": "Fatima",
        "age": 20
    },

    "Student5": {
        "name": "Fahad",
        "age": 22
    }
}

for student, details in students.items():
    print(student, ":", details)