class University:

    def __init__(self, name, city, students):
        self.name = name
        self.city = city
        self.students = students

    def display(self):
        print("University:", self.name)
        print("City:", self.city)
        print("Students:", self.students)


uni1 = University("COMSATS", "Islamabad", 12000)

uni1.display()