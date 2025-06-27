Distance = float(input("Enter the number1: \n"))
Time = float(input("Enter the number2: \n"))
Speed = Distance / Time
print("The Speed =", Speed)

if Speed >= 120.00:
    print("Overspeed")

elif 120 < Speed <= 80:
    print("The Speed in limits: follow Lane 3")
elif 65.00 < Speed <= 80.00:
    print("The Speed in limits: follow Lane 2")
elif 50.00 < Speed <= 65.00:
    print("The Speed in limits: follow Lane 1")
else:
    print("The Speed in limits: follow Service road")
