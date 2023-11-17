from typing import Sequence


def right_binary_search(array: Sequence[int | float], target: int | float) -> int | None:
    array_length = len(array)
    left = 0
    right = array_length - 1

    while left < right:
        middle = (left + right + 1) // 2
        if array[middle] <= target:
            left = middle
        else:
            right = middle - 1

    if array_length == 0 or array[left] > target:
        return None
    return left
