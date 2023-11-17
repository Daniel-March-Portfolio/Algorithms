from typing import Sequence

import pytest

from python.search.binary_search.strict_binary_search.realization import strict_binary_search


@pytest.mark.parametrize(
    "sequence,target,output",
    [
        [[1, 2, 3, 4, 5, 6], 1, 0],
        [[1, 2, 3, 4, 5, 6], 2, 1],
        [[1, 2, 3, 4, 5, 6], 3, 2],
        [[1, 2, 3, 4, 5, 6], 4, 3],
        [[1, 2, 3, 4, 5, 6], 5, 4],
        [[1, 2, 3, 4, 5, 6], 6, 5],
        [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 0.1, 0],
        [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 0.2, 1],
        [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 0.3, 2],
        [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 0.4, 3],
        [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 0.5, 4],
        [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 0.6, 5],
    ]
)
def test_for_sequence_with_even_length(sequence: Sequence[int | float], target: int | float, output: int | None):
    """
    Checks if the algorithm is working correctly for an even-length sequence.
    """
    assert strict_binary_search(sequence, target) == output


@pytest.mark.parametrize(
    "sequence,target,output",
    [
        [[1, 2, 3, 4, 5], 1, 0],
        [[1, 2, 3, 4, 5], 2, 1],
        [[1, 2, 3, 4, 5], 3, 2],
        [[1, 2, 3, 4, 5], 4, 3],
        [[1, 2, 3, 4, 5], 5, 4],
        [[0.1, 0.2, 0.3, 0.4, 0.5], 0.1, 0],
        [[0.1, 0.2, 0.3, 0.4, 0.5], 0.2, 1],
        [[0.1, 0.2, 0.3, 0.4, 0.5], 0.3, 2],
        [[0.1, 0.2, 0.3, 0.4, 0.5], 0.4, 3],
        [[0.1, 0.2, 0.3, 0.4, 0.5], 0.5, 4],
    ]
)
def test_for_sequence_with_odd_length(sequence: Sequence[int | float], target: int | float, output: int | None):
    """
    Checks if the algorithm is working correctly for an odd-length sequence.
    """
    assert strict_binary_search(sequence, target) == output


@pytest.mark.parametrize(
    "sequence,target,output",
    [
        [[1, 2, 3], 0, None],
        [[1, 2, 3, 4], 0, None],
        [[1, 2, 3], 5, None],
        [[1, 2, 3, 4], 5, None],
        [[0.1, 0.2, 0.3], 0.0, None],
        [[0.1, 0.2, 0.3, 0.4], 0.0, None],
        [[0.1, 0.2, 0.3], 0.5, None],
        [[0.1, 0.2, 0.3, 0.4], 0.5, None],
    ]
)
def test_for_sequence_without_target(sequence: Sequence[int | float], target: int | float, output: int | None):
    """
    Checks if the algorithm is working correctly for sequence that does not contain the target.
    """
    assert strict_binary_search(sequence, target) == output


def test_for_empty_sequence():
    """
    Checks if the algorithm is working correctly for an empty sequence.
    """
    assert strict_binary_search([], 0) is None
