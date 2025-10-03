class Movie:

    def __init__(self):
        self.age = 0

    def getData(self):
        self.age = float(input("Enter the age: \n"))

    def putData(self):
        print("The age is: \n", self.age)

    def discount(self):
        if 12 < self.age <= 65:
            Bill = 200
        else:

            Bill = 200 - (200 * 5) / 100
        print("The price is: \n", Bill)


M1 = Movie()
M1.getData()
M1.putData()
M1.discount()
