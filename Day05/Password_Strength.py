password = input("Enter Password: ")

upper = False
lower = False
digit = False

for ch in password:

    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

if upper and lower and digit and len(password) >= 8:
    print("Strong Password")

else:
    print("Weak Password")