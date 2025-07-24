from itertools import count
# fixed value, no editing, can use indexing and slicing, read only.

tup = (1, 4, 6.7, 1, 3)
print(tup)
lst=sorted(tup)
print(lst)

# len()
print(len(tup))

# max()
print(max(tup))
# min()
print(min(tup))

# index()
print(tup.index(3))  # index value of the element 3, and not index position 3

# count()
print(tup.count(1))

#sum()
print(sum(tup))

#tuple
print(tuple(lst))
