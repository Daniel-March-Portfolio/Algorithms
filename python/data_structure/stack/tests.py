import pytest

from python.data_structure.stack.realization import Stack


def test_push_and_list_methods():
    values = [1, 2, 3, 4]
    stack = Stack[int]()
    for value in values:
        stack.push(value)
    assert stack.list == values


def test_peak_method():
    values = [1, 2, 3, 4]
    stack = Stack[int]()
    for value in values:
        stack.push(value)
    assert stack.peek() == values[-1]
    assert stack.list == values


def test_pop_method():
    values = [1, 2, 3, 4]
    stack = Stack[int]()
    for value in values:
        stack.push(value)
    assert stack.pop() == values[-1]
    assert stack.list == values[:-1]


def test_is_empty_method():
    stack = Stack[int]()
    assert stack.is_empty is True
    stack.push(1)
    assert stack.is_empty is False


def test_clear_method():
    values = [1, 2, 3, 4]
    stack = Stack[int]()
    for value in values:
        stack.push(value)
    assert stack.is_empty is False
    stack.clear()
    assert stack.is_empty is True


def test_empty_stack_exception():
    stack = Stack[int]()
    with pytest.raises(ValueError, match="Stack is empty"):
        stack.pop()
    with pytest.raises(ValueError, match="Stack is empty"):
        stack.peek()
    stack.push(1)
    stack.peek()
    stack.pop()
    with pytest.raises(ValueError, match="Stack is empty"):
        stack.pop()
    with pytest.raises(ValueError, match="Stack is empty"):
        stack.peek()
