class Calculator:

    def __init__(self):
        self.Num1 = int(input("Enter first number: \n"))
        self.Num2 = int(input("Enter second number: \n"))

    def add(self):
        sum = self.Num1 + self.Num2
        print("The sum is: \n", sum)

    def sub(self):
        if self.Num1 > self.Num2:
            diff = self.Num1 - self.Num2
        else:
            diff = self.Num2 - self.Num1

        print("The difference is: \n", diff)

    def mul(self):
        if self.Num1 == 0 or self.Num2 == 0:
            print("Please enter non zero numbers \n")
        else:
            prod = self.Num1 * self.Num2
            print("The product is: \n", prod)

    def div(self):
        if self.Num1 == 0 or self.Num2 == 0:
            print("Please enter non zero numbers \n")
        else:
            quo = self.Num1 / self.Num2
            print("The quotient is: \n", quo)


Calc1 = Calculator()

while True:
    print("")
    print("Welcome to Calculator \n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): "))
    if choice == 5:
        print("Thank you.")
        break
    if choice > 5:
        print("Invalid Choice")
    if choice == 1:
        Calc1.add()
    elif choice == 2:
        Calc1.sub()
    elif choice == 3:
        Calc1.mul()
    else:
        Calc1.div()

def Armstrong(lst):
    nlst = []
    for i in lst:
        i = int(i)
        nlst.append(i)
    print(nlst)

    for i in nlst:

        add = 0
        iter = 1
        dup = i
        num = str(i)
        num_len = len(num)

        while i > 0:
            mod = i % 10
            add += mod ** num_len
            i = i // 10
            iter += 1
        print(add)

        if add == dup:
            print("Armstrong Number")

lst1=[153, 301]
print(Armstrong(lst1))

