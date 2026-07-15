class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


employee1 = Employee("Ahmed", 80000, "IT")

employee1.display()