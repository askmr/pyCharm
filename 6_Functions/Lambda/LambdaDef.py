# lambda args:exp

# sum of 2 numbers

sum = lambda a, b: a + b
print(sum(4, 5))

# square of a number
num = int(input("Enter number: \n"))
sqr = lambda num: num ** 2
print(sqr(num))

# average of 3 numbers

num1 = int(input("Enter number: \n"))
num2 = int(input("Enter number: \n"))
num3 = int(input("Enter number: \n"))

avg = lambda num1, num2, num3: (num1 + num2 + num3) / 3
print(avg(num1, num2, num3))
