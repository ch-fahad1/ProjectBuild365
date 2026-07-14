try:
    num = int(input("Enter an Integer: "))

    print("You Entered:", num)

except ValueError:
    print("Error: Please enter a valid integer.")