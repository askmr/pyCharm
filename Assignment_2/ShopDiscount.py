class Shop:
    def __init__(self):
        self.purchase = int(input("Enter purchase amount:"))

    def discount(self):
        if self.purchase > 5000:
            Dprice = self.purchase * 0.2
            print("Discount applied:", Dprice)
            Fprice = self.purchase - Dprice
            print("Final price:", Fprice)
        elif 2000 < self.purchase <= 5000:
            Dprice = self.purchase * 0.1
            print("Discount applied:", Dprice)
            Fprice = self.purchase - Dprice
            print("Final price:", Fprice)
        else:
            print("No Discount")
            print("Final price:", self.purchase)


S1 = Shop()
S1.discount()
