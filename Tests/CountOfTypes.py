from typing import Tuple


def count_types(s: str) -> Tuple[int, int, int]:
    letters = digits = specials = 0

    for i in s:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
        else:
            specials += 1
    return letters, digits, specials


print(count_types("Hello@123"))
