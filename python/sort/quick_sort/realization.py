from copy import deepcopy


def quick_sort(array: list[int | float]) -> list[int | float]:
    array_length = len(array)
    if array_length == 0:
        return []

    array: list[int | float] = deepcopy(array)

    less = []
    equal = []
    greater = []

    middle_idx = array_length // 2
    middle_element = array[middle_idx]
    for current_idx in range(array_length):
        current_element = array[current_idx]
        if current_element < middle_element:
            less.append(current_element)
        elif current_element > middle_element:
            greater.append(current_element)
        else:
            equal.append(current_element)

    return quick_sort(less) + equal + quick_sort(greater)
