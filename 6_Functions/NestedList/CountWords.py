fo = open('File1', 'r')
lst = fo.readlines() #Splits sentences lines by line, can have spaces
c = len(lst)
print(lst, c)

fo.seek(0)
w = fo.read().split() #Splits sentences lines by line, WITHOUT spaces
print()
wc = {}

for i in w:
    if i in wc:
        wc[i] += 1
    else:
        wc[i] = 1
print()
print("\n", w, "\n", wc)

for i, c in wc.items():
    print(i, c)
