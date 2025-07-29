lst = [1, 2, 3, 4, 5, 6]
nlst = ['tomato', 'onion', 'cabbage', 'brinjal']

# greater than 3
lst1 = list(filter(lambda x: x > 3, lst))
print(lst1)

# Even numbers
lst2 = list(filter(lambda x: x % 2 == 0, lst))
print(lst2)

# Odd numbers
lst3 = list(filter(lambda x: x % 2 != 0, lst))
print(lst3)

# multiples of 3
lst4 = list(filter(lambda x: x % 3 == 0, lst))
print(lst4)

nlst1 = list(filter(lambda x: len(x) > 6, nlst))
print(nlst1)

nlst2 = list(filter(lambda x: 'i' in x, nlst))
print(nlst2)
