try:
    num = int(input("Enter Number: "))

    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Program executed successfully.")