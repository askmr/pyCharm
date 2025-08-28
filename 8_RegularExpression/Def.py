# match()
# search()
# findall()
# sub()
import re

s = "enter The string"
t = "Enter"
st = 'hai 123 hello 567 how8 are9 you10     @#$ ABCDE QWERTY'

# r1 = re.match("The", s)  # case-sensitive by default, searches on FIRST word, so returns NONE.
# r2 = re.match(t, s, re.IGNORECASE)  # ignore case so now returned value.
# print('\n', r1, '\n', r2)
#
# r3 = re.search("The", s)  # searches entire string
# r4 = re.search(t, s, re.IGNORECASE)  # ignore case so now returned value.
# print('\n', r3, '\n', r4)
# print()

# expressions
# d

r5 = re.findall('\d', st)   #digits only, each item in list
r6 = re.findall('\d+', st)  #combined digits only, item in list
r7 = re.findall('\D', st)   #non digits, each item in list
r8 = re.findall('\D+', st)  #combined non digits, each item in list
print('\n', r5, '\n', r6, '\n', r7, '\n', r8)
print()

r9 = re.findall('\w', st)   #without spaces, no special
r10 = re.findall('\w+', st) #combined without spaces, no special
r11 = re.findall('\W', st)  #opposite of w, spaces and special only
r12 = re.findall('\W+', st) #opposite of w+. spaces and combined special
print('\n', r9, '\n', r10, '\n', r11, '\n', r12)
print()

r13 = re.findall('\s', st)  #space only
r14 = re.findall('\s+', st) #spaces only
r15 = re.findall('\S', st)  #similar to D, but without spaces
r16 = re.findall('\S+', st) #similar to D+, without spaces
print('\n', r13, '\n', r14, '\n', r15, '\n', r16)

#sub()
r17=re.sub('\d', "_", st)
print(r17)

r18=re.sub('[^\w\s]',"", st)
print(r18)


