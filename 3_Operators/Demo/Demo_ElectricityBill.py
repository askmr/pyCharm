unit = float(input("Enter the units consumed: \n"))

PaidUsage1 = unit - 100
PaidUsage2 = unit - 200
print("The PaidUsage is: \n", PaidUsage1)

if 100 <= PaidUsage1 <= 200:
    Bill = PaidUsage1 * 5
    print("The bill is: \n", Bill)

elif PaidUsage1 > 200:
    Bill1 = (PaidUsage1-PaidUsage2) * 5
    Bill2 = PaidUsage2 * 10
    Bill = Bill1 + Bill2
    print("The bill is: \n", Bill)
else:
    print("The bill is NIL")
