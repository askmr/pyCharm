# lst=[2,5,1,7,9,0]
lst = input("Enter the number: \n").split()
nlst1 = []
j = int(lst[0])
for i in lst:
    i = int(i)
    nlst1.append(i)
print(nlst1)

for i in nlst1:
    if i > j:
        j = i
print("largest number is", j)
