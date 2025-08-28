def maxFruits(lst):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    print(dct )

    maxC = 0
    maxF = ""

    for i in dct:
        if dct[i] > maxC:
            maxC = dct[i]
            maxF = i
    return maxF


lst = ["apple", "banana", "apple", "grape", "orange", "apple", "banana", "grape"]
print(maxFruits(lst))
