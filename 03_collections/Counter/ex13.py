from collections import Counter
from typing import Optional


def find_most_common_element(lst: list[int]) -> Optional[int]:
    if lst:
        return max(Counter(lst).items(), key=lambda x: x[1])[0]
    return None


assert find_most_common_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
assert find_most_common_element([3, 8, 7, 3, 3, 5, 3, 5, 1, 3, 3]) == 3
assert find_most_common_element([1, 2, 3]) == 1
assert find_most_common_element([5]) == 5
assert find_most_common_element([]) is None