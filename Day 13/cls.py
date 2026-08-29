import sys

class bankAccount:
    totalCurrency = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)

        if self.balance < 0:
            raise ValueError

        self.transactions = list()

        self.totalCurrency += self.balance

    def deposit_amt(self, amt):
        while True:
            if float(amt) <= 0:
                print("Invalid Operation, Deposit must be positive")
                amt = float(input("Amount to deposit (Enter 0 again to cancel): "))
                if amt == 0:
                    sys.exit(1)
                continue
            break

        self.balance += float(amt)

        self.transactions.append("Deposit: {}".format(amt))
        print("Successfully Deposited!")

    def withdraw_amt(self, amt):
        while True:
            if float(amt) <= 0:
                print("Invalid Operation, Withdraw must be positive")
                amt = float(input("Amount to Withdraw (Enter 0 again to cancel): "))
                if amt == 0:
                    sys.exit(1)
                continue
            break

        if self.balance - float(amt) < 0:
            print("Insufficient funds for withdrawal of that amount. Exiting...")
            sys.exit(1)
        else:
            self.balance -= float(amt)

        self.transactions.append("Withdraw: {}".format(amt))
        print("Successfully Withdrawn!")

    def transfer(self, target, amt):
        while True:
            if float(amt) <= 0:
                print("Invalid Operation, Transfer must be positive")
                amt = float(input("Amount to Transfer (Enter 0 again to cancel): "))
                if amt == 0:
                    sys.exit(1)
                continue
            break

        if self.balance - float(amt) < 0:
            print("Insufficient Funds for Transfer. Exiting...")
            sys.exit(1)

        try:
            self.balance -= amt
            target.balance += amt
        except:
            print("Transaction Failed, please try again...")

        self.transactions.append("Transfer: {}".format(amt))
        print("Successfully Transferred!")