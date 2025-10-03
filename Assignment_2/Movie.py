class Movie:
    def __init__(self):
        self.age = int(input("Enter age:"))

    def ticketPrice(self):
        if self.age < 12:
            price = 100
            print("Ticket price:", price)
        elif 12 <= self.age < 18:
            price = 150
            print("Ticket price:", price)
        else:
            price = 200
            print("Ticket price:", price)


M1 = Movie()
M1.ticketPrice()
