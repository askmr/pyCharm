class Account:

    def __init__(self):
        self.accNo = input("Enter account number: \n")
        self.accName = input("Enter account holder name: \n")
        self.accBranch = input("Enter branch name: \n")
        self.accType = input("Enter account type: \n")
        self.accBalance = float(input("Enter available balance: \n"))

    def deposit(self):
        amount = float(input("Enter amount to deposit: \n"))
        self.accBalance += amount
        print("Current balance is: \n", self.accBalance)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: \n"))

        if amount > self.accBalance:
            print("Insufficient Balance")
        else:
            self.accBalance -= amount
            print("Current balance is: \n", self.accBalance)

    def balanceEnquiry(self):
        print("Current balance is: \n", self.accBalance)

    def accountSummary(self):
        print("\n Account number=", self.accNo, "\n AccountName=", self.accName,
              "\n Branch=", self.accBranch, "\n AccountType=", self.accType,
              "\n Balance=", self.accBalance)


Acc1 = Account()

while True:
    print("Welcome to Bank of Luminar \n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Account Summary")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): "))
    if choice == 5:
        print("Thank you.")
        break
    if choice > 5:
        print("Invalid Choice")
    if choice == 1:
        Acc1.deposit()
    elif choice == 2:
        Acc1.withdraw()
    elif choice == 3:
        Acc1.balanceEnquiry()
    else:
        Acc1.accountSummary()
