lst1 = ['apple', 'orange', 'mango', 'grapes']

lst2 = list(map(lambda n: len(n), lst1))
# lst2 = list(map(len, lst1)) #Even this works

print(lst2)

lst3 = list(map(lambda n: n.capitalize(), lst1))
print(lst3)

lst4 = list(map(lambda n: n.upper(), lst1))
print(lst4)
