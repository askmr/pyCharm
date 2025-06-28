N1 = int(input("Enter the number1: \n"))
N2 = int(input("Enter the number2: \n"))
N3 = int(input("Enter the number3: \n"))

if N1 >= N2 and N1 >= N3:
    print("The number1 is Largest")
elif N2 >= N1 and N2 >= N3:
    print("The number2 is Largest")
else:
    print("The number3 is Largest")

if N1 <= N2 and N1 <= N3:
    print("The number1 is Smallest")
elif N2 <= N1 and N2 <= N3:
    print("The number2 is Smallest")
else:
    print("The number3 is Smallest")
