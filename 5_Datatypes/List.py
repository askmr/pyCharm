# lst1=[1,2,3,4,5,6,7,8,9,10]
#
# for i in lst1:
#     if i%2==0:
#         print(i)

# to create new list with even numbers

# lst2=[]
# for i in lst1:
#     if i%2==0:
#         lst2.append(i)
# print(lst2)

# remove duplicates, split a sentence, sotre in list
# lst1=[1,2,3,2,4,2,5,6,1]
# nlst=[]
# s="Python is simple"
# print(s.split())                            #to split a string and store in list
# for i in lst1:
#     if lst1.count(i)>=1 and i not in nlst:  #to remove duplicates in list
#         nlst.append(i)
# print(nlst)
# nlst.append(s.split())
# print(nlst)

# lst1 = input("Enter the data")  # to enter a string
# lst = lst1.split()  # to put into list #split() takes space by default
# nlst = []
# print(lst)
# for i in lst:
#     if type(i) == int:
#         if i % 2 == 0:
#             nlst.append(i)
# print(nlst)

