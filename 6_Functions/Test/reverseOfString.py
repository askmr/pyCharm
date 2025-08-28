def reverseStr(str):
    str = str[::-1]
    return str


def reverseNum(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev


str1 = 'string'
num1=12345
newWord = reverseStr(str1)
newNum = reverseNum(num1)
print(newWord, newNum)

