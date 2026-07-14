try:
    num = int(input("Enter Number: "))

    print(100 / num)

except Exception:
    print("Something went wrong.")

finally:
    print("Thank you for using the program.")