def countChar(text, char):
    c=0
    for i in text:
        if i == char:
            c+=1
    return c

result=countChar("Hello World", "l")
print(result)