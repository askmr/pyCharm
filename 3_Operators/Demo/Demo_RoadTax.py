N1 = int(input("Enter the number1: \n"))

if N1 >= 100000:
    tax = N1 * 15 / 100
    print("TAX=", tax)

elif 50000 <= N1 < 100000:
    tax = N1 * 10 / 100
    print("TAX=", tax)
elif N1 <= 50000:
    tax = N1 * 5 / 100
    print("TAX=", tax)
else:
    print("Number Invalid")
