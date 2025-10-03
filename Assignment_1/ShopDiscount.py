class Shop:
    def __init__(self):
        self.amount = 0

    def getData(self):
        self.amount = int(input("Enter total bill: \n"))

    def putData(self):
        print("Amount:\n", self.amount)


class Discount(Shop):
    def __init__(self):
        Shop.__init__(self)
        self.bill = 0

    def Bill(self):
        amt = self.amount

        if 1000 < amt < 2000:
            self.bill = amt - (0.1 * amt)
        elif 2001 < amt < 5000:
            self.bill = amt - (0.2 * amt)
        else:
            self.bill = amt - (0.3 * amt)

    def displayBill(self):
        print("Total bill is:\n", self.bill)


disc1 = Discount()
disc1.getData()
disc1.putData()
disc1.Bill()
disc1.displayBill()
