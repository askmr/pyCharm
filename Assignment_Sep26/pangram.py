def pangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    str = str.lower()

    for i in alphabet:
        if i not in str:
            return False
    return True

str1 = 'The quick brown fox jumps over a lazy dog'
str2 = 'A quick brown fox jumps over a lazy dog'
print(pangram(str1))
print(pangram(str2))