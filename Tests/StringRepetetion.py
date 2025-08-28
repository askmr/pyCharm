def repeated_string(s: str, n: int) -> int:
    countA_In_s = s.count('a')

    countOfs_In_n = n // len(s)
    countA_In_n = countA_In_s * countOfs_In_n

    remainder = n % len(s)
    countA_Remainder = s[:remainder].count('a')

    return countA_In_n + countA_Remainder


# asdsas 10 times, 10 floor division length of s which is 6, so quo is 1, mod is 4, output is 2 * 1 + 1
# abcac 10 times, 10 floor division length of s which is 5, so quo is 2, mod is 0, output is 2 * 2 + 0

print(repeated_string('abcac', 10))
