def substring(str):
    x=1
    for i in str:
        if i.isdigit() and i!='0':
            x*=int(i)
    return x

str='a0b2c3'
mul=substring(str)
print(mul)