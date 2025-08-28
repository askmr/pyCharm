import re

g1=open("gen1", "w+")
g1.writelines(["!@#$%^ 123456 qwerty QWERTY &*()"])
g1.seek(0)
data=g1.read()
print(data)
print(g1)

#remove special char
g2=re.sub('[^\w\s]', '', data)
print(g2)
c1=len(g2)
print(c1)

#replace numbers with special char
g3=re.sub('[\d+\s]', '!', data)
print(g3)
c2=len(g3)
print(c2)
# g1.close()

# count of words
g4=re.sub('[1-9!@#$%^&*()]', '', data)
lst4=g4.split()
print(lst4)
c3=len(lst4)
print(c3)

#capital and small letters
g5=re.findall('[A-Z]', data)
print(g5, len(g5))
g6=re.findall('[a-z]', data)
print(g6, len(g6))

#close
#reopen
#write
#close

