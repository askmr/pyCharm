def Armstrong(lst):
    nlst = []
    for i in lst:
        i = int(i)
        nlst.append(i)
    print(nlst)

    for i in nlst:

        add = 0
        iter = 1
        dup = i
        num = str(i)
        num_len = len(num)

        while i > 0:
            mod = i % 10
            add += mod ** num_len
            i = i // 10
            iter += 1
        print(add)

        if add == dup:
            print("Armstrong Number")

lst1=[153, 301]
print(Armstrong(lst1))


# def fact(num):
#     f=1
#     for i in range(1, num +1):
#         f*=i
#     print(f)
#
# print(fact(6))

# def addMul5(lst):
#     nlst1 = list(map(lambda n: n if n%5==0 else 0, lst))
#     add = 0
#     # for i in lst:  # for i in range(1, num+1)
#     #     if i % 5 == 0:
#     #         nlst1.append(i)
#     # print(nlst1)
#
#     for i in nlst1:
#         add += i
#     return add
#
#
# lst1 = [5, 10, 15, 20, 25, 30, 35, 40, 11, 23, 44, 67, 74, 97]
# num=addMul5(lst1)
# print(num)
