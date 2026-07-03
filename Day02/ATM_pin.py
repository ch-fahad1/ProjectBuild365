correct_pin = "1234"

for attempt in range(1, 4):

    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break

    else:
        print("Incorrect PIN")

else:
    print("Your ATM Card has been Blocked.")