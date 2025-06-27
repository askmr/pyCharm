# Celsius to Farenheit, also round the result to 2 decimels
# F = C*9/5 +32

Celsius = float(input("Enter Celsius: \n"))
Fahrenheit = (Celsius * (9 / 5)) + 32

print("The Fahrenheit is: \n", Fahrenheit)
print("The Fahrenheit is: \n", round(Fahrenheit, 2))
