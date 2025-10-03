class Notes:
    def __init__(self):
        self.amount=int(input("Enter amount: \n"))

    def dispatch(self):
        if self.amount >= 2000:
            n1 = self.amount // 2000
            self.amount= self.amount % 2000
            print("2000:", n1)
        if self.amount >= 500:
            n2 = self.amount // 500
            self.amount= self.amount % 500
            print("500:", n2)
        if self.amount >= 10:
            n3 = self.amount // 10
            self.amount= self.amount % 10
            print("10:", n3)

N1=Notes()
N1.dispatch()