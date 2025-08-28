def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def product(a, b):
    return a * b


def division(a, b):
    return a / b


def perimeter(a, b):
    return 2 * (a + b)


def area(a, b):
    if a == b:
        return a ** 2
    else:
        return a * b


def opposite(str):
    str1 = ""
    for i in str:
        if i.isupper():
            str1 += i.lower()
        elif i.islower():
            str1 += i.upper()
        else:
            str1 += i
    return str1

def capital(str):
    str1=""

    for i in str:
        if i in str[0] and i.islower():
            str1 += i.upper()
        else:
            str1 += i
    return str1