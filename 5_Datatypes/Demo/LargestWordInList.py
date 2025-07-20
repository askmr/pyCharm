lst = ['asd', 'asde', 'werfd', 'qwerty']
lar = lst[0]

for i in lst:
    if len(i) > len(lst[0]):
        lar = i
print(lar)
