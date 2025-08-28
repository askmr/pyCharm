def findLCM(a, b, c):
    num = max(a, b, c)

    while True:
        if num % a == 0 and num % b == 0 and num % c == 0:
            return num
        num += 1


a, b, c = 4, 5, 10
lcm = findLCM(a, b, c)
print(lcm)
