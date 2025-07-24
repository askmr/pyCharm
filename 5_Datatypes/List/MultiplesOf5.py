lst=input("Enter numbers: \n").split()

nlst1=[]
nlst2=[]
nlst3=[]
for i in lst:
    i = int(i)
    nlst1.append(i)
print(nlst1)

for i in nlst1:
    if i%5==0:
        nlst2.append(i)
print(nlst2)

for i in nlst2:
    if i not in nlst3:
        nlst3.append(i)
print(nlst3)