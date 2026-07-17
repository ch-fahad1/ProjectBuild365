class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit Successful")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount()

account.deposit(5000)

account.withdraw(1500)

account.show_balance()