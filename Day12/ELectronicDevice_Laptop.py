class ElectronicDevice:

    def power_on(self):
        print("Device Powered On")


class Laptop(ElectronicDevice):

    def code(self):
        print("Coding in Python")


laptop = Laptop()

laptop.power_on()

laptop.code()