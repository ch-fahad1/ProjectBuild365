class Laptop:

    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display(self):
        print("Brand:", self.brand)
        print("Processor:", self.processor)
        print("RAM:", self.ram)


laptop1 = Laptop("HP", "Core i7", "16GB")

laptop1.display()