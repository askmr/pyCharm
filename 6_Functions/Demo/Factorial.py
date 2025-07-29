# Method 1
# user input

def fact():
    num = int(input("Enter the number: \n"))
    f = 1
    for i in range(1, num + 1):
        f *= i
    print(f)


fact()


# Method 2
# with args

def fact1(num):
    # num = int(input("Enter the number: \n"))
    f = 1
    for i in range(1, num + 1):
        f *= i
    print(f)


fact1(6)
