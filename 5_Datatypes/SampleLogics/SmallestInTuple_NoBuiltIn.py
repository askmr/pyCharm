# tup = (6, 7, 8, 9, 0, 3, 45, 56)
# lst=sorted(tup)
# print(lst)
# # s=min(tup)
# s=lst.index(0)
# print(s)

tup = input("Enter the numbers: \n").split()
lst= sorted(tup)

nlst1 = []
j = int(lst[0])
for i in lst:
    i = int(i)
    nlst1.append(i)
print(nlst1)

for i in nlst1:
    if i < j:
        j = i
print("Smallest number is", j)