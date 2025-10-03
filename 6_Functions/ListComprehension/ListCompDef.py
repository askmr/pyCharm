lst = [1, 2, 3, 4, 5]

# for loop with conditions, filters out values.
lst1 = [i * i for i in lst if i % 2 == 1]  # SQUARE
print(lst1)
lst2 = [i * 2 for i in lst if i % 2 == 0]  # DOUBLE
print(lst2)

# for loop with conditions, without filtering the values.
lst3 = [i * i if i % 2 == 1 else i for i in lst]
print(lst3)

# ONLY using for loop
lst4 = [i * i for i in lst]
print(lst4)
