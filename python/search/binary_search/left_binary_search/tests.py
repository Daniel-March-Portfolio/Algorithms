from typing import Sequence

import pytest

from python.search.binary_search.left_binary_search.realization import left_binary_search


@pytest.mark.parametrize(
    "sequence,target,output",
    [
        [[0, 0, 1, 1, 2, 2], 0, 0],
        [[0, 0, 1, 1, 2, 2], 1, 2],
        [[0, 0, 1, 1, 2, 2], 2, 4],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.1, 0],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.2, 1],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.3, 1],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.4, 2],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.5, 2],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.6, 3],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.7, 3],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.8, 4],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 0.9, 4],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 1.0, 5],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1], 1.1, 5]
    ]
)
def test_for_sequence_with_even_length(sequence: Sequence[int | float], target: int | float, output: int | None):
    """
    Checks if the algorithm is working correctly for an even-length sequence.
    """
    assert left_binary_search(sequence, target) == output


@pytest.mark.parametrize(
    "sequence,target,output",
    [
        [[0, 0, 0, 1, 1, 2, 2], 0, 0],
        [[0, 0, 0, 1, 1, 2, 2], 1, 3],
        [[0, 0, 0, 1, 1, 2, 2], 2, 5],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.1, 0],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.2, 1],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.3, 1],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.4, 2],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.5, 2],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.6, 3],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.7, 3],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.8, 4],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 0.9, 4],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 1.0, 5],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 1.1, 5],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 1.2, 6],
        [[0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3], 1.3, 6]
    ]
)
def test_for_sequence_with_odd_length(sequence: Sequence[int | float], target: int | float, output: int | None):
    """
    Checks if the algorithm is working correctly for an odd-length sequence.
    """
    assert left_binary_search(sequence, target) == output


@pytest.mark.parametrize(
    "sequence,target,output",
    [
        [[1, 2, 3], 0, 0],
        [[1, 2, 3], 4, None],
        [[1.2, 1.3, 1.4], 1.1, 0],
        [[1.2, 1.3, 1.4], 1.5, None]
    ]
)
def test_for_sequence_without_target(sequence: Sequence[int | float], target: int | float, output: int | None):
    """
    Checks if the algorithm is working correctly for sequence that does not contain the target.

    For sequence = [1, 2, 3] and target = 0:
    returns '0' because '1' is the first number that is greater than or equal to '0'

    For sequence = [1, 2, 3] and target = 4:
    returns 'None' because the sequence does not contain a number that is greater than or equal to '4'

    For sequence = [1.2, 1.3, 1.4] and target = 1.1:
    returns '0' because '1.2' is the first number that is greater than or equal to '1.1'

    For sequence = [1.2, 1.3, 1.4] and target = 1.5:
    returns 'None' because the sequence does not contain a number that is greater than or equal to '1.5'
    """
    assert left_binary_search(sequence, target) == output


def test_for_empty_sequence():
    """
    Checks if the algorithm is working correctly for an empty sequence.
    """
    assert left_binary_search([], 0) is None
