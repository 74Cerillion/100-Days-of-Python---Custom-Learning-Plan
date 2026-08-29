import sys
from cls import bankAccount

inst = {
    "jsnuffy": bankAccount("Joe Snuffy", 200),
    "hspeed": bankAccount("High Speed", 400),
    "ldrag": bankAccount("Low Drag", 600),
    "whoo": bankAccount("Woo Hoo", 800),
}

def main():
    print("WELCOME! To begin, please sign in:\n")
    user = input("Enter your username: ")

    while True:
        if user in inst.keys():
            break
        else:
            print("User does not exist.")
            sys.exit(1)

    print("Please choose an action from the following menu:\n")
    print(r"""
    1: Deposit Funds
    2: Withdraw Funds
    3: Transfer Funds
    """)

    while True:
        action = input("Enter Desired Action (CHOOSE NUMBER): ")
        if action == 'q':
            sys.exit(1)
        if int(action) in [1, 2, 3]:
            break
        else:
            print("Invalid Action. Enter valid action or press 'q' to quit.")

    if int(action) == 1:
        amount = float(input("Amount to Deposit: "))
        inst[user].deposit_amt(float(amount))

    if int(action) == 2:
        amount = float(input("Amount to Withdraw: "))
        inst[user].withdraw_amt(float(amount))

    if int(action) == 3:
        amount = float(input("Amount to Transfer: "))
        target = input("Transfer to: ")

        if target not in inst:
            print("Target account does not exist.")
            sys.exit(1)

        inst[user].transfer(inst[target], float(amount))

    print("Thank you for being a member of our <bank name>\nCome again soon!")

if __name__ == '__main__':
    main()