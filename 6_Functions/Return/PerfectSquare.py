def isSquare(num):
    if num < 0:
        return False
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False


num = int(input("Enter the number: \n"))
if isSquare(num):
    print("Perfect Square")
