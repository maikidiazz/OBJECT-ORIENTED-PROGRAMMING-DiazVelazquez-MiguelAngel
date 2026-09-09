class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposito bien exitoso.")
        else:
            print("The deposit must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal.")

    def check_balance(self):
        print("Current balance:", self.__balance)


# creacion de las cuentas
account1 = BankAccount("Pedro Chacon", 5000)
account2 = BankAccount("Albertito Bravito", 3000)


# cuenta 1
print("Aaccount holder:", account1.holder)
account1.check_balance()

account1.deposit(1000)
account1.withdraw(500)

print("Updated balance:")
account1.check_balance()


print("__-_____-____-_____--____")


# cuenta 2
print("Account holder:", account2.holder)
account2.check_balance()

account2.deposit(500)
account2.withdraw(200)

print("Updated balance:")
account2.check_balance()