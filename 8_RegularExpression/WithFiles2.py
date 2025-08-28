import re

g1=open("gen2", "w+")
g1.writelines(["see the sky \n she is dancing \n Shoe is blank in color \n is earth Round in shape"])
g1.seek(0)
data=g1.read()
print(data)
print(g1)

pattern1 = re.findall('s\we', data) #for one letter \w, for many letters use \w+
print(pattern1, len(pattern1))
pattern2 = re.findall('s\w+e', data)
print(pattern2, len(pattern2))
pattern3 = re.findall('[A-Z]\w+', data)
print(pattern3, len(pattern3))
pattern4 = re.findall("[a-zA-Z]{5}", data)
print(pattern4, len(pattern4))