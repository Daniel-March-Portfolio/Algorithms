from dataclasses import dataclass

import pytest

from python.search.breadth_first_search.realization import Node, breadth_first_search

TARGET_NODE = Node(val=100)


@dataclass
class Data:
    empty_tree = None
    single_node_tree = TARGET_NODE
    single_branch_tree = Node(val=1,
                              children=[
                                  Node(val=2,
                                       children=[
                                           Node(val=3,
                                                children=[
                                                    TARGET_NODE
                                                ])
                                       ])
                              ])
    wide_tree = Node(val=1,
                     children=[
                         Node(val=2),
                         Node(val=3),
                         TARGET_NODE,
                         Node(val=5),
                     ])
    normal_tree = Node(val=1,
                       children=[
                           Node(val=2,
                                children=[
                                    Node(val=4),
                                    Node(val=5,
                                         children=[
                                             TARGET_NODE,
                                         ]),
                                ]),
                           Node(val=3,
                                children=[
                                    Node(val=6),
                                    Node(val=7),
                                    Node(val=8),
                                ]),
                       ])


@pytest.mark.parametrize(
    "tree,target,output",
    [
        [Data.single_node_tree, 100, TARGET_NODE],
        [Data.single_branch_tree, 100, TARGET_NODE],
        [Data.wide_tree, 100, TARGET_NODE],
        [Data.normal_tree, 100, TARGET_NODE],
    ]
)
def test_if_target_exists(tree: Node, target: int, output: Node):
    """
    Checks whether the algorithm works correctly for a tree with a target.
    """
    assert breadth_first_search(tree, target) == output


@pytest.mark.parametrize(
    "tree,target",
    [
        [Data.single_node_tree, 101],
        [Data.single_branch_tree, 101],
        [Data.wide_tree, 101],
        [Data.normal_tree, 101],
    ]
)
def test_if_target_does_not_exists(tree: Node, target: int):
    """
    Checks whether the algorithm works correctly for a tree without a target.
    """
    assert breadth_first_search(tree, target) is None


def test_for_empty_tree():
    """
    Check if the algorithm works correctly for an empty tree.
    """
    assert breadth_first_search(Data.empty_tree, 1) is None
