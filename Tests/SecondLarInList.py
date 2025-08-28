from typing import List


def second_largest(lst: List[int]) -> int:
    nlst1 = []

    for i in lst:
        if i not in nlst1:
            nlst1.append(i)
            nlst1.sort(reverse=True)
    return nlst1[1]


print(second_largest([10, 20, 30, 40, 50, 20, 30, 40]))
