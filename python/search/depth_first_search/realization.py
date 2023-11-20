from dataclasses import dataclass
from typing import Sequence, Self


@dataclass
class Node:
    val: int
    children: Sequence[Self] = ()


def depth_first_search(node: Node, val: int) -> Node | None:
    if node is None or node.val == val:
        return node
    for child in node.children:
        if child and (child := depth_first_search(child, val)):
            return child
    return None
