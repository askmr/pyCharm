fo = open('File1', 'r')
print("Location of pointer: \n", fo.tell())  # position at starting character
print(fo.read(1))

print("Location of pointer: \n", fo.tell())  # pointer incremented to next character
print(fo.read(1))

print("Location of pointer: \n", fo.tell())

fo.seek(5)  # pointer directly to index
print("Location of pointer: \n", fo.tell())  # position at index
print(fo.read())

fo.seek(0)
print("Location of pointer: \n", fo.tell())  # position back to 0
print(fo.readline())
# fo.close()
print(fo.readline())
print(fo.readlines())
print("Location of pointer: \n", fo.tell())

fo.seek(0)
lst=fo.readlines()
c=len(lst)
print(lst, c)