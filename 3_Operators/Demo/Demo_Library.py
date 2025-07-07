Days = float(input("Total days visited in Library: \n"))

if 0 <= Days <= 5:
    Charges = Days * 2
    print("The total charges= \n", Charges)

elif 6 <= Days <= 10:
    Days1 = Days - 5
    Charges = (Days-Days1) * 2 + Days1 * 3
    print("The total charges= \n", Charges)

elif 11 <= Days <= 15:
    Days1 = Days - 5
    Days2 = Days - 10
    Charges = (Days1 - Days2) * 2 + (Days1 - Days2) * 3 + Days2 * 4
    print("The total charges= \n", Charges)
elif 15 < Days:
    Days1 = Days - 5
    Days2 = Days - 10
    Days3 = Days - 15
    Charges = (Days1 - Days2) * 2 + (Days1 - Days2) * 3 + (Days1 - Days2) * 4 + Days3 * 5
    print("The total charges= \n", Charges)

else:
    print("The bill is NIL")
