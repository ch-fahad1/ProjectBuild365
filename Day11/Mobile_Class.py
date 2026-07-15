class Mobile:

    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)


mobile1 = Mobile("Samsung", "8GB", "256GB")

mobile1.display()