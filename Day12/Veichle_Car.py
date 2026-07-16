class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car is Driving")


car = Car()

car.start()
car.drive()