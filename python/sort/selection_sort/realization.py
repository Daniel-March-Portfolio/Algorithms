from copy import deepcopy


def selection_sort(array: list[int | float]) -> list[int | float]:
    array_length = len(array)
    array: list[int | float] = deepcopy(array)

    for updating_idx in range(array_length - 1):
        minimal_element_idx = updating_idx
        for current_element_idx in range(updating_idx + 1, array_length):
            if array[current_element_idx] < array[minimal_element_idx]:
                minimal_element_idx = current_element_idx
        if minimal_element_idx != updating_idx:
            array.insert(updating_idx, array.pop(minimal_element_idx))
    return array
