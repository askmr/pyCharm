class ATM:
    def __init__(self):
        self.balance = int(input("Enter Account balance: \n"))

    def balanceEnquiry(self):
        print("Account balance: \n", self.balance)

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: \n"))

        if amount > self.balance:
            print("Insufficient funds")
        elif amount % 100 != 0:
            print("Invalid denomination")
        else:
            self.balance-=amount
            print("Transaction successful! \n Remaining Balance:", self.balance)

A1= ATM()
A1.balanceEnquiry()
A1.withdraw()


