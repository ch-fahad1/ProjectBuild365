try:
    password = input("Enter Password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    print("Password Accepted.")

except ValueError as error:
    print(error)