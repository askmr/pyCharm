def charStr():
    x = 0
    str = input("Enter string: \n")
    c = input("Enter char: \n")
    lst1 = []
    for i in str:
        lst1.append(i)
        if i == c:
            x = lst1.index(i)
    return x


def remChar1():
    y = 0
    str = input("Enter string: \n")
    c = int(input("Enter index: \n"))
    lst1 = []
    for i in str:  # to convert word into elements in list using for loop (without using list() )
        lst1.append(i)
    lst1.pop(c)  # to delete item at index position c (without using del() )
    str1 = ""
    for j in lst1:  # to join elements in list into a string/word
        str1 += j
    return str1


def remChar2(text, index):
    return text[:index] + text[index + 1:]  # splicing at index position "start:index" and "index+1:end"


def remChar3(text, index):
    lst1 = list(text)  # char in word, into list using list ()
    del lst1[index]  # to delete item at index position using del()
    return ''.join(lst1)  # to directly join a list into a string/word


x = charStr()
print(x)
print()
y = remChar1()
print(y)
print()
z = remChar2('word', 3)
print(z)
print()
w = remChar3('word', 2)
print(w)
