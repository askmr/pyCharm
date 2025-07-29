# FACTORIAL using return
#
def Fact1():
    n = int(input("Enter number1: \n"))
    f = 1

    for i in range(1, n + 1):
        f *= i
    print("First factorial is:", f)


def Fact2(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    print("Second factorial is:", f)


def Fact3():
    f = 1
    n = int(input("Enter number3: \n"))

    for i in range(1, n + 1):
        f *= i
    return f


def Fact4(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


Fact1()
Fact2(5)
print()
f1 = Fact3()
print("Third factorial is:", f1)
f2 = Fact4(6)
print("Fourth factorial is:", f2)
