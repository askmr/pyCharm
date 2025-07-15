n = int(input("Enter number: \n"))  # ARMSTRONG number
s = 0
i = 1
m = n
num=str(n)
num_dig= len(num)

while n > 0:
    a = n % 10
    print(i, "Mod value is", a)
    s+=a**num_dig
    print(i, "current sum=", s)
    n = n // 10
    i += 1
print("Final sum=", s)
if s == m:
    print("Armstrong number")
else:
    print("NOT an armstrong number")