from copy import deepcopy
from typing import Any


def _swap(array: list[Any], first_index: int, second_index: int) -> None:
    array[first_index], array[second_index] = array[second_index], array[first_index]


def bubble_sort(array: list[int | float]) -> list[int | float]:
    array: list[int | float] = deepcopy(array)
    array_length=len(array)

    for end_of_unsorted_array in range(array_length, 0, -1):
        for idx in range(end_of_unsorted_array - 1):
            if array[idx] > array[idx + 1]:
                _swap(array, idx, idx + 1)
    return array
