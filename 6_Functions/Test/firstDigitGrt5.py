str='32Python629'
nlst1=[]
for i in str:
    if i.isdigit() and int(i) > 5:
        nlst1.append(i)
        break
print(nlst1)
