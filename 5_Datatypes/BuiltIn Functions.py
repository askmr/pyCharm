list1 = [1, 9, 2, 6, 3, 4, 4]
print(list1)  # print the list
print(len(list1))  # total elements
print(max(list1))  # biggest element (only for integers)
print(min(list1))  # smallest number (only for integers)
print(list1.index(4))  # position of the element
print(list1.count(4))  # occurance of the element

list1.append(10)  # to add element at the end
print(list1)
list1.extend([27, 54, 81])
print(list1)  # to add multiple element at the end
list1.insert(2, 25)
print(list1)  # to add element at a particular index

list1.pop()
print(list1)  # to remove element
list1.pop(2)
print(list1)  # to remove element at a particular index
list1.remove(10)
print(list1)  # to remove a particular element

# list2.clear()
# print(list2)

list2 = ["AA", "abcA", "Aa", "aa", "aAc", "aaC", "5"]
list2.sort()  # sorting, based on ordinal value
print(list2)
list2.sort(reverse=True)
print(list2)
