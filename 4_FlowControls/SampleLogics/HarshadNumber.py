n = int(input("Enter number: \n"))  # Harshad number
s = 0
i = 1
m = n
while n > 0:
    a = n % 10
    print(i, "Mod value is", a)
    s+=a
    print(i, "current sum=", s)
    n = n // 10
    i += 1
print("Final sum=", s)
if m%s == 0:
    print(m, "is a Harshad number")
else:
    print(m, "is NOT a Harshad number")