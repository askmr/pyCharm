# Celsius to Farenheit, also round the result to 2 decimels
# F = C*9/5 +32

# Celsius = float(input("Enter Celsius: \n"))
# Fahrenheit = (Celsius * (9 / 5)) + 32
#
# print("The Fahrenheit is: \n", Fahrenheit)
# print("The Fahrenheit is: \n", round(Fahrenheit, 2))

choice = int(input("Enter your choice: \n "
                   "1. Fahrenheit to Celsius \n "
                   "2. Celsius to Fahrenheit \n"))

if choice == 1:
    Fahrenheit = float(input("Enter Fahrenheit: \n"))
    Celsius = (Fahrenheit - 32) * 5 / 9

    print("The Fahrenheit is: \n", Fahrenheit)
    print("The Celsius is: \n", round(Celsius, 2))

elif choice == 2:
    Celsius = float(input("Enter Celsius: \n"))
    Fahrenheit = (Celsius * (9 / 5)) + 32

    print("The Celsius is: \n", Celsius)
    print("The Fahrenheit is: \n", round(Fahrenheit, 2))

else:
    print("INVALID input \n")
