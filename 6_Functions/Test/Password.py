def passwordCheck(str):
    c=0
    n=0
    u=0
    l=0

    for i in str:
        if i.isdigit():
            n+=1
            c+=1
        elif i.isupper():
            u+=1
            c+=1
        elif i.islower():
            l+=1
            c+=1
        else:
            print("Please dont add special char")

    return c, n, u, l

str= 'qwertyQ123'
char, num, upper, lower= passwordCheck(str)
print(passwordCheck(str))
if char > 8 and upper >= 1 and lower >= 1 and num >= 1:
    print("Password is eligible")
else:
    print("Password NOT eligible")


