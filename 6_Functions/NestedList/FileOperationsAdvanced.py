f4 = open(r'C:\Users\HP\Documents\File4.txt', 'w+') # opened a NEW file to read and write
f4.writelines(["College", "\n", "School\n"])
f4.seek(0)
data=f4.read()
print(data)
f4.close()