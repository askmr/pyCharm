class Employee:
    def __init__(self):
        self.name = input("Enter employee name: \n")
        self.hours = int(input("Enter hours worked: \n"))
        self.rate = int(input("Enter wage (per hr): \n"))

    def allowance(self):
        if self.hours > 40:
            extraTime = self.hours - 40
            regularPay = 40 * self.rate
            overtimePay = extraTime * self.rate * 1.5
            totalPay = regularPay + overtimePay
            print()
            print("Employee: ", self.name)
            print("Regular Pay: ", regularPay)
            print("Overtime Pay: ", overtimePay)
            print("Total Pay: ", totalPay)
        else:
            regularPay = self.hours * self.rate
            print("Employee: ", self.name)
            print("Regular Pay: ", regularPay)


E1 = Employee()
E1.allowance()
