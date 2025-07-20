lst=input("Enter the numbers: \n").split()
olist=[]
elist=[]
nlist1=[]
nlist2=[]
s1=0
s2=0

for i in lst:
    i = int(i)
    nlist1.append(i)
print(nlist1)
print()

for i in nlist1:
    if i%2==0:
        elist.append(i)
        s1+=i #s1= sum(elist)

    else:
        olist.append(i)
        s2+=i #s2= sum(olist)

print("Even list=", elist, "\n Sum= ", s1)
print()
print("Odd list=", olist, "\n Sum= ", s2)

