def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


f = fact(6)
print(f)


def sumOfNatural(x):
    if x == 0:
        return 0
    else:
        return x + sumOfNatural(x - 1)


add = sumOfNatural(5)
print(add)
