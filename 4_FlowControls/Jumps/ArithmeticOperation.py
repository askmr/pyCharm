while True:
    print("Welcome to Arithmetic operations.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): "))
    if choice == 5:
        print("Thank you.")
        break
    if choice > 5:
        print("Invalid Choice")
        break

    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))

    if choice == 1:
        print("The sum of numbers is", Num1 + Num2)
        print()
    elif choice == 2:
        if Num1 > Num2:
            print("The difference of numbers is", Num1 - Num2)
            print()
        else:
            print("The difference of numbers is", Num2 - Num1)
            print()
    elif choice == 3:
        print("The product of numbers is", Num1 * Num2)
        print()
    else:
        if Num1 != 0 and Num2 != 0:
            print("The division of numbers is", Num1 / Num2)
            print()
        else:
            print("Cannot divide when number is a zero")
            print()
