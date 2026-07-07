import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(num):
    if num < 0:
        return "Invalid Number"
    return math.sqrt(num)

def percentage(obtained, total):
    return (obtained / total) * 100


while True:

    print("\n===== Smart Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", add(a, b))

    elif choice == 2:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", subtract(a, b))

    elif choice == 3:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", multiply(a, b))

    elif choice == 4:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", divide(a, b))

    elif choice == 5:
        a = float(input("Base: "))
        b = float(input("Power: "))
        print("Answer =", power(a, b))

    elif choice == 6:
        a = float(input("Enter Number: "))
        print("Answer =", square_root(a))

    elif choice == 7:
        obtained = float(input("Obtained Marks: "))
        total = float(input("Total Marks: "))
        print("Percentage =", percentage(obtained, total), "%")

    elif choice == 8:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

    again = input("\nDo you want another calculation? (Y/N): ")

    if again.upper() != "Y":
        print("Goodbye!")
        break