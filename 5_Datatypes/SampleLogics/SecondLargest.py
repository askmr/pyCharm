# find the second-largest number
lst = input("Enter numbers: \n").split()
nlst1=[]
nlst2=[]
for i in lst:
    i = int(i)
    nlst1.append(i)
print(nlst1)

for i in nlst1:
    if i not in nlst2:  #to remove duplicates in list
        nlst2.append(i)
print(nlst2)
nlst2.sort(reverse=True)
print(nlst2)

if nlst2[1] < nlst2[0]:
    print(nlst2[1])
