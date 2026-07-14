try:
    age = int(input("Enter Age: "))

    if age < 18:
        raise ValueError("You must be at least 18 years old.")

    print("You are eligible.")

except ValueError as error:
    print(error)