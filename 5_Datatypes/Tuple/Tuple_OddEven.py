tup = (6, 7, 8, 9, 0, 3, 45, 56)

lst1 = sorted(tup)
elst = []
olst = []
print(lst1)

for i in lst1:
    if i % 2 == 0:
        elst.append(i)
    else:
        olst.append(i)
print(elst, "= List of Even numbers")
print(olst, "= List of Odd numbers")

etup = tuple(elst)
otup = tuple(olst)

print(etup, "= Tuple of Even numbers")
print(otup, "= Tuple of Odd numbers")

lst2 = elst + olst
tup2 = tuple(lst2)

print(tup2)
