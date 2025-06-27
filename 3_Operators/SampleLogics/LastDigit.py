# Print the last digit of a given number

number = float(input("Enter the number: \n"))
lastDigit = number % 10
print("The last digit is: \n", lastDigit)

if lastDigit % 3==0:
    print("The last digit is divisible by 3")


