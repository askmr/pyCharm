class Temperature:
    def __init__(self):
        self.degrees = 0

    def getData(self):
        self.degrees = float(input("Enter temperature: \n"))

    def putData(self):
        print("Temperature (in Celsius): \n", self.degrees)


class Advice(Temperature):
    def __init__(self):
        Temperature.__init__(self)
        self.condition = ""

    def roomCondition(self):
        temp = self.degrees

        if temp <= 10:
            self.condition = "Cold"
        elif 10 < temp <= 25:
            self.condition = "Pleasant"
        else:
            self.condition = "Hot"

    def displayTemp(self):
        print("The condition of room is:", self.condition, "\n at", self.degrees, "degrees")


AD1 = Advice()
AD1.getData()
AD1.putData()
AD1.roomCondition()
AD1.displayTemp()
