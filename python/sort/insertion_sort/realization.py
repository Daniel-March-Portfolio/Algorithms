from copy import deepcopy


def insertion_sort(array: list[int | float]) -> list[int | float]:
    array: list[int | float] = deepcopy(array)
    array_length = len(array)

    for end in range(1, array_length):
        for idx in range(end - 1, -1, -1):
            if array[end] > array[idx]:
                array.insert(idx + 1, array.pop(end))
                break
        else:
            array.insert(0, array.pop(end))
    return array
