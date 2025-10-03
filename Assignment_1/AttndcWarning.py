class Attendance:
    def __init__(self):
        self.percentage = 0

    def getData(self):
        self.percentage = float(input("Enter percentage: \n"))

    def putData(self):
        print("Attendance (in %): \n", self.percentage)


class Eligibility(Attendance):
    def __init__(self):
        Attendance.__init__(self)
        self.warning = ""

    def status(self):
        value = self.percentage

        if value < 75:
            self.warning = "Warning: Low Attendance"
        else:
            self.warning = "Eligible"

    def displayStatus(self):
        print(self.warning)

Eg1 = Eligibility()
Eg1.getData()
Eg1.putData()
Eg1.status()
Eg1.displayStatus()