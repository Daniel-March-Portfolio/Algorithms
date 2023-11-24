import pytest

from python.data_structure.queue.realization import Queue


def test_push_and_list_methods():
    values = [1, 2, 3, 4]
    queue = Queue[int]()
    for value in values:
        queue.push(value)
    assert queue.list == values


def test_peak_method():
    values = [1, 2, 3, 4]
    queue = Queue[int]()
    for value in values:
        queue.push(value)
    assert queue.peek() == values[0]
    assert queue.list == values


def test_is_empty_method():
    queue = Queue[int]()
    assert queue.is_empty is True
    queue.push(1)
    assert queue.is_empty is False


def test_pop_method():
    values = [1, 2]
    queue = Queue[int]()
    for value in values:
        queue.push(value)
    assert queue.pop() == values[0]
    assert queue.list == values[1:]
    assert queue.pop() == values[1]
    assert queue.is_empty is True


def test_clear_method():
    values = [1, 2, 3, 4]
    queue = Queue[int]()
    for value in values:
        queue.push(value)
    assert queue.is_empty is False
    queue.clear()
    assert queue.is_empty is True


def test_empty_queue_exception():
    queue = Queue[int]()
    with pytest.raises(ValueError, match="Queue is empty"):
        queue.pop()
    with pytest.raises(ValueError, match="Queue is empty"):
        queue.peek()
    queue.push(1)
    queue.peek()
    queue.pop()
    with pytest.raises(ValueError, match="Queue is empty"):
        queue.pop()
    with pytest.raises(ValueError, match="Queue is empty"):
        queue.peek()
