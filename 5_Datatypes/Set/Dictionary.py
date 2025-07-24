#dct_name[key]=value
#dct={key:value} , name in ''. name is case sensitivity

dct={'name':'Atul', 'RollNo': 10}
print(dct)

dct['place']='Kollam'
dct['RollNo']=47
print()
print(dct, "\n Length is:", len(dct))
print()
print(dct.keys())
print(dct.values())
print(dct.items())
print()
print(dct.get('place'))

for i in dct.items():
    print(i)

dct.update({'School': 'Kendriya Vidyalaya', 'College': 'Anna University'})
print(dct)

dct.popitem()
print(dct)

dct.pop('School')
print(dct)

