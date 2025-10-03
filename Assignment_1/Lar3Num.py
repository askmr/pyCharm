lar = lambda num1, num2, num3: num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)
num1 = int(input("Enter number: \n"))
num2 = int(input("Enter number: \n"))
num3 = int(input("Enter number: \n"))

print(lar(num1, num2, num3))
