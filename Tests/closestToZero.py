def closeToZero(num):
    closest = num[0]

    for n in num:
        if (n >= 0 and closest < 0) or \
            (n < 0 and closest < 0 and n > closest) or \
            (n >=0 and closest >= 0 and n < closest)or \
            (n < 0 and closest >= 0 and -n < closest):

            closest = n
    return closest

array = [5,-2, 1, 8, -1]

print(closeToZero(array))