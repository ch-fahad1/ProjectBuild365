def create_account():

    try:

        # Take Input

        name = input("Enter Name: ").strip()

        if name == "":
            raise ValueError("Name cannot be empty.")

        account_number = input("Enter Account Number: ").strip()

        if account_number == "":
            raise ValueError("Account Number cannot be empty.")

        balance = float(input("Enter Initial Balance: "))

        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        # Check Duplicate Account

        try:

            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) >= 2:

                        if account_number == data[1]:

                            print(" Account Number Already Exists.")
                            return

        except FileNotFoundError:

            pass

        # Save Account

        with open("accounts.txt", "a") as file:

            file.write(f"{name},{account_number},{balance}\n")

        print(" Account Created Successfully!")

    except ValueError as error:

        print("Error:", error)


def deposit():

    try:

        account_number = input("Enter Account Number: ").strip()

        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        found = False

        with open("accounts.txt", "w") as file:

            for line in lines:

                data = line.strip().split(",")

                if account_number == data[1]:

                    new_balance = float(data[2]) + amount

                    file.write(f"{data[0]},{data[1]},{new_balance}\n")

                    print(" Deposit Successful!")
                    print("New Balance:", new_balance)

                    found = True

                else:

                    file.write(line)

        if not found:
            print(" Account Not Found.")

    except FileNotFoundError:
        print("No Accounts Exist Yet.")

    except ValueError as error:
        print("Error:", error)


def withdraw():

    try:

        account_number = input("Enter Account Number: ").strip()

        amount = float(input("Enter Withdraw Amount: "))

        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0.")

        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        found = False

        with open("accounts.txt", "w") as file:

            for line in lines:

                data = line.strip().split(",")

                if account_number == data[1]:

                    balance = float(data[2])

                    if amount > balance:

                        print(" Insufficient Balance!")

                        file.write(line)

                    else:

                        new_balance = balance - amount

                        file.write(f"{data[0]},{data[1]},{new_balance}\n")

                        print("✅ Withdrawal Successful!")
                        print("Remaining Balance:", new_balance)

                    found = True

                else:

                    file.write(line)

        if not found:
            print("❌ Account Not Found.")

    except FileNotFoundError:
        print("No Accounts Exist Yet.")

    except ValueError as error:
        print("Error:", error)


def check_balance():

    account_number = input("Enter Account Number: ").strip()

    found = False

    try:

        with open("accounts.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if account_number == data[1]:

                    print("\n===== Account Details =====")
                    print("Name :", data[0])
                    print("Account Number :", data[1])
                    print("Balance :", data[2])

                    found = True
                    break

        if not found:
            print("Account Not Found.")

    except FileNotFoundError:

        print("No Accounts Exist Yet.")

while True:

    print("\n====== Bank Management System ======")

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    choice = input("Enter Your Choice: ")

    if choice == "1":

     create_account()

    elif choice == "2":

        deposit()

    elif choice == "3":

        withdraw()

    elif choice == "4":

        check_balance()

    elif choice == "5":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")