n = int(input("Enter number: \n"))  #sum of digits in number
s=0
i=1
while n >= 1 and i < n:
    a = n%10
    print(i, "Mod value is", a)
    s+=a
    print(i, "current sum=", s)
    n= n//10

    print(i, "new number is", n)
    i+=1
print("Final sum=", s+n)

# n = int(input("Enter number: \n"))  #sum of digits in number WITHOUT i
# s=0
# i=1
# while n > 0:
#     a = n%10
#     print(i, "Mod value is", a)
#     s+=a
#     print(i, "current sum=", s)
#     n= n//10
# print("Final sum=", s)

n = int(input("Enter number: \n"))  #sum of CUBE of digits
i=1
while n > 0:
    a = n%10
    print(i, "Mod value is", a)
    s+=a**3
    print(i, "current sum=", s)
    n= n//10
print("Final sum=", s)
