from copy import deepcopy


def _merge(first_subarray: list[int | float], second_subarray: list[int | float]) -> list[int | float]:
    result = []
    while len(first_subarray) > 0 and len(second_subarray) > 0:
        if first_subarray[0] < second_subarray[0]:
            result.append(first_subarray.pop(0))
        else:
            result.append(second_subarray.pop(0))
    return result + first_subarray + second_subarray


def merge_sort(array: list[int | float]) -> list[int | float]:
    array: list[int | float] = deepcopy(array)
    array_length = len(array)

    middle = array_length // 2
    if array_length < 2:
        return array
    elif array_length > 2:
        first_subarray = merge_sort(array[:middle])
        second_subarray = merge_sort(array[middle:])
    else:
        first_subarray= [array[0]]
        second_subarray = [array[1]]

    result = _merge(first_subarray, second_subarray)
    return result
