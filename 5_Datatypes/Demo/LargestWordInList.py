# lst=input("Enter the strings: \n").split()
lst = ['asd', 'asde', 'werfdE', 'qwerty']

maxL = len(lst[0])

for i in lst:
    if len(i) > maxL:
        maxL = len(i)
print(maxL)

for i in lst:
    if len(i) == maxL:
        print(i)

    # lst1 = [1, 2, 3, 4, 5]
    # add = 0
    #
    # for i in lst1:
    #     add += i
    # print(add)
