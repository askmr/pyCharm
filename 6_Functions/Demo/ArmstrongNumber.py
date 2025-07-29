def ArmstrongNum(lst):
    nlst1 = []
    for i in lst:
        i = int(i)
        nlst1.append(i)
    print(nlst1)

    for i in nlst1:
        add = 0
        dup = i
        iter = 1
        num = str(i)
        numLen = len(num)
        while i > 0:
            mod = i % 10
            print(iter, "Mod value is", mod)
            add += mod ** numLen
            print(iter, "current sum=", add)
            i = i // 10
            iter += 1
        print("Final sum=", add)
        if add == dup:
            print("Armstrong")


lst = input("Enter the numbers").split()
ArmstrongNum(lst)
