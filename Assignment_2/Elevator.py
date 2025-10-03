class Elevator:
    def __init__(self):
        self.floor = 0

    def operation(self):
        while True:
            print("Welcome to Luminar Apartments")
            print("1. Select Floor")
            print("2. Stop")

            choice = int(input("Enter your choice: \n"))
            if choice == 1:
                self.floor = int(input("Enter Floor(1-10): \n"))
                if self.floor <= 10:
                    print("\n Moving to:", self.floor, "\n")
                else:
                    print("Invalid floor")
            if choice == 2:
                print("Stop")
                break


E1 = Elevator()
E1.operation()
