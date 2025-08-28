from typing import List


def find_duplicates(lst: List[int]) -> List[int]:
    nlst1 = []

    for i in lst:
        if i not in nlst1:
            nlst1.append(i)
    return nlst1


print(find_duplicates([1, 2, 3, 4, 1, 2, 5, 2, 1]))
