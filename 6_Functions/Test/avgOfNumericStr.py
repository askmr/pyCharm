def avg(str):
    c = 0
    total = 0
    for i in str:
        if i.isdigit():
            total += int(i)
            c += 1
    if c == 0:
        return 0
    return total / c


str = '15abc42'
print(avg(str))
