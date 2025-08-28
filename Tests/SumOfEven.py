from typing import List


def sum_even_numbers(lst: List[int]) -> int:
    total = 0
    add = lambda a, b: a + b
    for num in lst:
        if num % 2 == 0:
            total = add(total, num)
    return total


print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
