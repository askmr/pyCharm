n = int(input("Enter number: \n"))  # ARMSTRONG number
s = 0
i = 1
m = n
while n > 0:
    a = n % 10
    print(i, "Mod value is", a)
    s += a ** 3
    print(i, "current sum=", s)
    n = n // 10
    i += 1
print("Final sum=", s)
if s == m:
    print(m, "is an armstrong number")
else:
    print(m, "is NOT an armstrong number")

#######EXPERIMENT for n= 3 digit and 4 digit numbers.
# print(i-1)
# n=m
# j=i
# i=1
# if j == 3:
#     while n > 0:
#         a = n % 10
#         print(i, "Mod value is", a)
#         s += a ** 3
#         print(i, "current sum=", s)
#         n = n // 10
#         i += 1
# elif j==4:
#     while n > 0:
#         a = n % 10
#         print(i, "Mod value is", a)
#         s += a ** 4
#         print(i, "current sum=", s)
#         n = n // 10
#         i += 1
# print("Final sum=", s)
# if s == m:
#     print(m, "is an armstrong number")
# else:
#     print(m, "is NOT an armstrong number")
################################################


for i in range(100, 1000):
    s = 0
    n = i
    while i > 0:
        d = i % 10
        s = s + d ** 3
        i = i // 10
    if n == s:
        print(n)
