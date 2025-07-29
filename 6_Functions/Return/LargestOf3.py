def retVal(n1, n2, n3):
    lar = 0
    if n1 > n2 and n1 > n3:  # means n1 is largest
        lar = n1

    elif n2 > n3:  # means n2 is largest, no need other operations
        lar = n2
    else:
        lar = n3

    return lar


n1 = int(input("Enter first number: \n"))
n2 = int(input("Enter second number: \n"))
n3 = int(input("Enter third number: \n"))

largest = retVal(n1, n2, n3)
print(largest)
