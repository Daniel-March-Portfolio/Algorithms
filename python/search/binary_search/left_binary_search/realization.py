from typing import Sequence


def left_binary_search(array: Sequence[int], target: int) -> int | None:
    array_length = len(array)
    left = 0
    right = array_length

    while left < right:
        middle = (left + right) // 2
        if array[middle] >= target:
            right = middle
        else:
            left = middle + 1

    return left if left < array_length else None
