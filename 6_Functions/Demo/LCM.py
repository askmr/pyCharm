def LCM(n1, n2):
    if n1 >= n2:
        lar = n1
    else:
        lar = n2

    while True:
        if lar % n1 == 0 and lar % n2 == 0:
            print("LCM is: ", lar)
            break
        else:
            lar += 1

n1 = int(input("Enter first number: \n"))
n2 = int(input("Enter second number: \n"))
LCM(n1, n2)