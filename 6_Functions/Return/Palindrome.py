# Panidrome

def isPalindrome(str):
    str1 = str.lower()
    rev_str = str1[::-1]
    return rev_str


word = input("Enter a word: \n")
if isPalindrome(word):
    print("Palindrome")
