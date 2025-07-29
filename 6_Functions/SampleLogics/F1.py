# named, reusable block of code, designed for a specific task

# with user input
def sumFun():
    num1 = int(input("Enter first number: \n"))
    num2 = int(input("Enter second number: \n"))

    add = num1 + num2
    print("The sum is: \n", add)


sumFun()


# with args
def sumFun(num1, num2):  # Formal Args
    add = num1 + num2
    print("The sum is: \n", add)


sumFun(89, 45)  # Actual Args


# Average of 2 numbers
def average(num1, num2):
    add = num1 + num2
    avg = add / 2
    print("The sum is: \n", add)
    print("The average is: \n", avg)


average(25, 35)
