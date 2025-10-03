def remVowel(str):
    vowels='aeiouAEIOU'
    return "".join([x for x in str if x not in vowels])

str='Programming'
print(remVowel(str))