class Gym:
    def __init__(self):
        self.plan= input("Enter plan (Standard/Premium): \n")
        self.months= int(input("Enter months: \n"))

    def subscription(self):
        if self.plan.lower() == "standard":
            if self.months <= 6:
                cost = self.months * 1500
                print("Total Bill: ", cost)
            else:
                cost1 = self.months * 1500
                discount = self.months * 1500 * 0.15
                totalCost = cost1 - discount
                print("Total Bill: ", totalCost)

        elif self.plan.lower() == "premium":
            if self.months <= 6:
                cost = self.months * 2500
                print("Total Bill: ", cost)
            else:
                cost1 = self.months * 2500
                discount = self.months * 2500 * 0.15
                totalCost = cost1 - discount
                print("Total Bill: ", totalCost)
        else:
            print("Invalid plan")


G1= Gym()
G1.subscription()