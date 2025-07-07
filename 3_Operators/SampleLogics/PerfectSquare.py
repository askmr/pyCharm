import math

N1 = int(input("Enter the number1: \n"))

lastDigit = N1 % 10
if lastDigit in (0, 1, 4, 5, 6, 9):
    root = math.isqrt(N1)
    # root = N1**0.5
    if type(root) == int:
        print("The number is a perfect square of \n", root)
    else:
        print("The number is NOT a perfect square \n")
else:
    print("The number is NOT a perfect square \n")
