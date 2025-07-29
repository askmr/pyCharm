# HOMEWORK-use dictionary, user definition for practice

# lst1=[]
# def num(lst):
#     for i in lst:
#         strlen = len(i)
#         print(strlen)
#         if strlen%2==0:
#             i = i.upper()
#             lst1.append(i)
#     print(lst1)

lst = ['apple', 'orange', 'mango', 'banana']

lst1 = list(map(lambda x: x.upper() if len(x) % 2 == 0 else x, lst))
print(lst1)

lst3 = list(map(lambda x: x.upper() if len(x) == 5 else x, lst))
print(lst3)

lst2 = list(map(lambda x: x.upper() if 'o' in x else x, lst))
print(lst2)
