def noRepeat(str):
    for i in str:
        if str.count(i)==1:
            return i
    return None

str1='swiss'
str2='coldplay'
str3='millenium'

print(noRepeat(str1))
print(noRepeat(str2))
print(noRepeat(str3))