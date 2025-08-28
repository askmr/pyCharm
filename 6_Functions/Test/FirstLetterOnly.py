def firstLetter(lst):
    nlst=[]
    for i in lst:
        words=i.split()
        abb=''.join([j[0].upper() for j in words if len(j)>2])
        nlst.append(abb)
    return nlst

lst1=['National Institute of Technology' , 'College of Engineering Technology']
print(firstLetter(lst1))
