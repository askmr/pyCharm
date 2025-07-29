result = lambda num1: "Positive" if num1 > 0 else ("Negative" if num1 < 0 else "Zero")
num1 = int(input("Enter number: \n"))

print(result(num1))
