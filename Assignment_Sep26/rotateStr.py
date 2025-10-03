def rotateStr(str, index):
    return str[index:] + str[:index]

str='abcdef'
index=2

print(rotateStr(str, index))