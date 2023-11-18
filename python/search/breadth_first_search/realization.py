from dataclasses import dataclass
from typing import Self, Sequence


@dataclass
class Node:
    val: int
    children: Sequence[Self] = ()


def breadth_first_search(root: Node | None, val: int) -> Node | None:
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        if node is None:
            continue
        if node.val == val:
            return node
        nodes.extend(node.children)
    return None
