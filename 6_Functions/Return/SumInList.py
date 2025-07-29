def sumInList(num):
    add = 0
    for i in num:
        add += i
    return add


def larNum(num):
    lar = num[0]
    for i in num:
        if i > lar:
            lar = i
    return lar


lst1 = [3, 2, 1, 4, 5]
total = sumInList(lst1)
large = larNum(lst1)
print(total)
print(large)


# for user input list, for loop will change for largest number, above wont work.
def larNum(num):
    lar = int(num[0])
    for i in num:
        j = int(i)
        if j > lar:
            lar = j
    return lar


lst2 = input("Enter the numbers: \n").split()
large = larNum(lst2)
print(large)
