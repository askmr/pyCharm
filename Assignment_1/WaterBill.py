class MeterCharges:
    def __init__(self):
        self.litres = 0

    def getData(self):
        self.litres = int(input("Enter water usage: \n"))

    def putData(self):
        print("Usage in litres: \n", self.litres)


class WaterBill(MeterCharges):
    def __init__(self):
        MeterCharges.__init__(self)
        self.bill = 0

    def discount(self):
        litres = self.litres

        if litres <= 500:
            self.bill = 0.5 * litres
        elif 500 < litres < 1000:
            self.bill = 0.75 * litres
        else:
            self.bill = 1 * litres

    def displayBill(self):
        print("Total bill is:\n", self.bill)


WB1 = WaterBill()
WB1.getData()
WB1.putData()
WB1.discount()
WB1.displayBill()
