# dct = {'EmpID': '112', 'empName': 'Anil'}
#
# dct.update({'Salary': 25000, 'Designation': 'Analyst'})
# print(dct)
#
# dct['Salary'] += 1000
# print(dct)
#
# dct.pop('Designation')
# print(dct)
#
# dct.popitem()
# print(dct)
#
# num = int(input("Enter limit: \n"))
#
# #Method 1
# lst1 = []
# lst2 = []
# for i in range(1, num + 1):
#     lst1.append(i)
# print(lst1)
#
# for i in lst1:
#     j = i ** 2
#     lst2.append(j)
# print(lst2)
#
# dct = dict(zip(lst1, lst2))
# print(dct)
#
# #Method 2
# dic={}
# for i in range(1, num + 1):
#     dic[i]=i ** 2
# print(dic)

lst3 = ['apple', 'orange', 'banana', 'mango', 'apple', 'banana', 'apple']

# Display item and item count into a dictionary

# Method 1- using BuiltIn function count
# dic1={}
# c=0
# for i in lst3:
#     c=lst3.count(i)
#     print(c)
#     dic1[i]=c
# print(dic1)

# Method 2- using BuiltIn function zip
# dic2 = {}
# lst4 = []
# lst5 = []
# for i in lst3:
#     c = 1
#     if i not in lst4:
#         lst4.append(i)
#         c+=1
#     else:
#         c+=1
#         lst5.append(c)
# print(lst4, lst5)
# print()
# print(dict(zip(lst4,lst5)))

# Method 3- without BuiltIn
dctC={}

for i in lst3:
    if i in dctC:
        dctC[i] += 1
    else:
        dctC[i] = 1
print(dctC)