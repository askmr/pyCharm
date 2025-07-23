setA = {2, 3, 4, 5}
setB = setA.copy()
setC = {3, 4, 5, 6}
setD = {5, 6, 7, 8}
print("\n", setA, setB, "\n", setC, setD)

setE = setC.union(setD)         # combine with duplicates removed
setF = setC.intersection(setD)  # common items only
setG = setC.difference(setD)    # bigger set minus common elements in smaller
setH = setD.difference(setC)    # bigger set minus common elements in smaller

setI = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}

print()
print(setE)
print(setF)         #
print(setG)
print(setH)
print(set(setI))    #remove duplicates in set
