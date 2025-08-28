from typing import List


def find_missing_number(lst: List[int]) -> int:
    addLst = sum(lst)

    lenLst = len(lst) + 1
    total = lenLst * (lenLst + 1) // 2

    missingNum = total - addLst
    return missingNum


print(find_missing_number([1, 2, 4, 5]))
