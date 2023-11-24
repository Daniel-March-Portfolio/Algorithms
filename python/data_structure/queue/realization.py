from dataclasses import dataclass
from typing import Any, TypeVar, Generic, Optional

__all__ = ["Queue"]

T = TypeVar("T")


@dataclass
class Node:
    value: Any
    next: Optional["Node"]
    previous: Optional["Node"]


class Queue(Generic[T]):
    def __init__(self):
        self.__linked_list_head: Node | None = None
        self.__linked_list_tail: Node | None = None

    def clear(self) -> None:
        self.__linked_list_head = None

    def peek(self) -> T:
        if self.is_empty:
            raise ValueError("Queue is empty")
        return self.__linked_list_head.value

    def pop(self) -> T:
        if self.is_empty:
            raise ValueError("Queue is empty")
        value = self.__linked_list_head.value
        self.__linked_list_head = self.__linked_list_head.next
        if id(self.__linked_list_head) == id(self.__linked_list_tail):
            self.__linked_list_tail.previous = None
        elif self.is_empty:
            self.__linked_list_tail = None
        return value

    def push(self, value: T) -> None:
        new_node = Node(
            value=value,
            previous=self.__linked_list_tail,
            next=None,
        )
        if self.is_empty:
            self.__linked_list_head = new_node
        else:
            self.__linked_list_tail.next = new_node

        self.__linked_list_tail = new_node

    @property
    def is_empty(self) -> bool:
        return self.__linked_list_head is None

    @property
    def list(self) -> list[T]:
        _list: list[T] = []
        linked_list_head = self.__linked_list_head
        while linked_list_head is not None:
            _list.append(linked_list_head.value)
            linked_list_head = linked_list_head.next
        return _list
