n = int(input("Enter number: \n"))  # ARMSTRONG number
s = 0
x = 1

m = n
num = str(n)
num_dig = len(num)

while n > 0:
    a = n % 10
    print(x, "Mod value is", a)
    s += a ** num_dig
    print(x, "current sum=", s)
    n = n // 10
    x += 1
print("Final sum=", s)
if s == m:
    print("Armstrong number")
else:
    print("NOT an armstrong number")
