# def addMul5(num):
#     lst1 = []
#     add = 0
#     for i in range(1, num + 1):
#         if i % 5 == 0:
#             lst1.append(i)
#     print(lst1)
#
#     for i in lst1:
#         add += i
#     print(add)
#
#
# num = int(input("Enter the number: \n"))
# addMul5(num)

#METHOD 2
def addMul5(num):
    add = 0
    lst1 = list(map(lambda x: x if x % 5 == 0 else 0, num))
    print(lst1)

    for i in lst1:
        add += i
    print(add)


num = [5, 12, 10, 15, 20, 25]
addMul5(num)