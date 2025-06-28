Number = int(input("Enter the number1: \n"))

if Number <=365:

    if Number % 7 == 1 or Number == 1:
        print("Sunday")
    elif Number % 7 == 2 or Number == 2:
        print("Monday")
    elif Number % 7 == 3 or Number == 3:
        print("Tuesday")
    elif Number % 7 == 4 or Number == 4:
        print("Wednesday")
    elif Number % 7 == 5 or Number == 5:
        print("Thursday")
    elif Number % 7 == 6 or Number == 6:
        print("Friday")
    elif Number % 7 == 0 or Number == 0:
        print("Saturday")

else:
    print("INVALID")
