# prints sorted numbers
# removes duplicates
# no indexes
# 1 and True in a set, is considered duplicate, similarly 0 and False, with and 0 and 1 having priority.
# can be edited, except frozen sets

setA = {0, 1, 2, 4, 2, 6, 5, 3, 'a', 'd', 'g', 'a', 1, 2, True, False}
print(setA)
print(len(setA))

setA.add(45)
print(setA)

setA.update(({7, 8, 9, 100}))
print(setA)

setA.pop()  # removes first element
print(setA)

setA.remove(45)  # Remove an element, also use discard()
print(setA)
