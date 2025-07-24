lst=input("Enter the strings: \n").split()

nlst1=[]
nlst2=[]

for i in lst:
    nlst1= list(i)
    if len(nlst1)>=3:
        nlst2.append(i)
print(nlst2)