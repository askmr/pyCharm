# n = int(input("Enter number: \n"))  # Harshad number
# s = 0
# i = 1
# m = n
# while n > 0:
#     a = n % 10
#     print(i, "Mod value is", a)
#     s+=a
#     print(i, "current sum=", s)
#     n = n // 10
#     i += 1
# print("Final sum=", s)
# if m%s == 0:
#     print(m, "is a Harshad number")
# else:
#     print(m, "is NOT a Harshad number")

ll = int(input("enter lower limit:"))
ul = int(input("enter upper limit:"))

num = ll

while num <= ul:
    temp = num
    sum = 0
    for i in str(temp):
        sum+=int(i)

    print("Final sum=", sum)
    if num%sum == 0:
        print(num, "is a Harshad number")
    num+=1

    # for i in range(ll, ul+1):
    #     n=i
    #     s=0
    #
    #     while i>0:
    #         d=i%10
    #         s+=d
    #         i=i%10
    #     if n%s==0:
    #         print(n)