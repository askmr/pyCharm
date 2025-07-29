num1 = int(input("Enter principal: \n"))
num2 = int(input("Enter ROI: \n"))
num3 = int(input("Enter tenure: \n"))

avg = lambda num1, num2, num3: (num1 * num2 * num3) / 100
print(avg(num1, num2, num3))
