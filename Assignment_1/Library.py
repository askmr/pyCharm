class Library:
    def __init__(self):
        self.days = 0

    def getData(self):
        self.days = int(input("Enter number of days late: \n"))

    def putData(self):
        print("Amount:\n", self.days)


class Latefees(Library):
    def __init__(self):
        Library.__init__(self)
        self.fees = 0

    def Fees(self):
        days = self.days

        if 1 < days <= 5:
            self.fees = self.fees + days * 5
        elif 6 < days <= 10:
            self.fees = self.fees + days * 7
        else:
            self.fees = self.fees + days * 10

    def displayFees(self):
        print("Total fees is:\n", self.fees)


Fees1 = Latefees()
Fees1.getData()
Fees1.putData()
Fees1.Fees()
Fees1.displayFees()
