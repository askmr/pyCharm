#
# lar = lambda num1, num2, num3: num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)
# num1 = int(input("Enter number: \n"))
# num2 = int(input("Enter number: \n"))
# num3 = int(input("Enter number: \n"))
#
# print(lar(num1, num2, num3))

def largest(lst):
    lar=lst[0]
    maxm=lambda a,b: a if a > b else b
    for i in lst[1:]:
        lar=maxm(lar,i)
    return lar

lst=[123,2,1,6,9,12]
num=largest(lst)
print(num)