from copy import deepcopy

from python.sort.counting_sort.realization import counting_sort


def test_for_array_with_even_length():
    """
    Checks if the algorithm is working correctly for an even-length array.
    """
    array = [6, 4, 5, 1, 2, 4, 5, 1, 2, 3, 0, 5, 0, 2, 1, 5]
    output = [0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    assert counting_sort(array) == output


def test_for_array_with_odd_length():
    """
    Checks if the algorithm is working correctly for an odd-length array.
    """
    array = [6, 4, 5, 1, 2, 4, 5, 1, 2, 3, 0, 5, 0, 2, 1, 5, 0]
    output = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    assert counting_sort(array) == output


def test_if_algorithm_is_not_in_place():
    """
    Checks whether the algorithm does not change the input array.
    """
    array = [6, 4, 5, 1, 2, 4, 5, 1, 2, 3, 0, 5, 0, 2, 1, 5]
    control_array = deepcopy(array)
    assert counting_sort(array) != array
    assert array == control_array


def test_for_empty_array():
    """
    Checks if the algorithm is working correctly for an empty array.
    """
    array = []
    output = []
    assert counting_sort(array) == output
