from dataclasses import dataclass
from typing import Any, TypeVar, Generic

__all__ = ["Stack"]

T = TypeVar("T")


@dataclass
class Node:
    value: Any
    next: "Node"


class Stack(Generic[T]):
    def __init__(self):
        self.__linked_list_head: Node | None = None

    def clear(self) -> None:
        self.__linked_list_head = None

    def peek(self) -> T:
        if self.is_empty:
            raise ValueError("Stack is empty")
        return self.__linked_list_head.value

    def pop(self) -> T:
        if self.is_empty:
            raise ValueError("Stack is empty")
        value = self.__linked_list_head.value
        self.__linked_list_head = self.__linked_list_head.next
        return value

    def push(self, value: T) -> None:
        new_linked_list_head = Node(
            value=value,
            next=self.__linked_list_head
        )
        self.__linked_list_head = new_linked_list_head

    @property
    def is_empty(self) -> bool:
        return self.__linked_list_head is None

    @property
    def list(self) -> list[T]:
        reversed_list: list[T] = []
        linked_list_head = self.__linked_list_head
        while linked_list_head is not None:
            reversed_list.append(linked_list_head.value)
            linked_list_head = linked_list_head.next
        return reversed_list[::-1]
