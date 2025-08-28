class Perfect:
    def __init__(self):
        self.Num1 = int(input("Enter first number: \n"))

        for i in range(1, self.Num1):  # perfect number
            fs = 0
            for j in range(1, i):
                if i % j == 0:
                    fs = fs + j
            if fs == i:
                print(i, "is a perfect number")

perf1=Perfect()