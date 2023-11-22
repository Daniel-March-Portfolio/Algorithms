def counting_sort(array: list[int]) -> list[int]:
    if len(array) == 0:
        return []

    minimal_element = min(array)
    maximal_element = max(array)
    counter = [0] * (maximal_element - minimal_element + 1)

    for element in array:
        counter[element - minimal_element] += 1

    result = []
    for offsetted_element, count in enumerate(counter):
        result += [offsetted_element + minimal_element] * count
    return result

# 54
# 43
