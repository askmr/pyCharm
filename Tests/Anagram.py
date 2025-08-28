def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


print(is_anagram("listen", "silent"))
print(is_anagram("hello World", "worhe llold"))
print(is_anagram("hello ", "World "))
