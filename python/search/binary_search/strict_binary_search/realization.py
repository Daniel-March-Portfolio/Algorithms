from typing import Sequence


def strict_binary_search(array: Sequence[int | float], target: int | float) -> int | None:
    array_length = len(array)
    left = 0
    right = array_length

    while left < right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    if array_length != 0 and array[left] == target:
        return left
    return None
