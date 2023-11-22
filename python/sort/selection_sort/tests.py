from copy import deepcopy

from python.sort.selection_sort.realization import selection_sort


def test_for_array_with_even_length():
    """
    Checks if the algorithm is working correctly for an even-length array.
    """
    array = [3, 1.5, 2.5, 3.5, 2, 0]
    output = [0, 1.5, 2, 2.5, 3, 3.5]
    assert selection_sort(array) == output


def test_for_array_with_odd_length():
    """
    Checks if the algorithm is working correctly for an odd-length array.
    """
    array = [3, 1.5, 2.5, 3.5, 2, 0, 1]
    output = [0, 1, 1.5, 2, 2.5, 3, 3.5]
    assert selection_sort(array) == output


def test_if_algorithm_is_not_in_place():
    """
    Checks whether the algorithm does not change the input array.
    """
    array = [3, 1.5, 2.5, 3.5, 2, 0, 1]
    control_array = deepcopy(array)
    assert id(selection_sort(array)) != id(array)
    assert array == control_array


def test_for_empty_array():
    """
    Checks if the algorithm is working correctly for an odd-length array.
    """
    array = []
    output = []
    assert selection_sort(array) == output
