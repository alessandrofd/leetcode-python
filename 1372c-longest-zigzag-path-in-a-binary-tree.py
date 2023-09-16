"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).

    If the current direction is right, move to the right child of the current
    node; otherwise, move to the left child.

    Change the direction from right to left or from left to right.

    Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node
has a length of 0).

Return the longest ZigZag path contained in that tree.

Constraints:
    The number of nodes in the tree is in the range [1, 5 * 104].
    1 <= Node.val <= 100
"""


from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


def to_binary_tree(nodes: List[int]) -> Optional[TreeNode]:
    """Cria uma árvore binária a partir de uma lista de nós"""

    if not nodes:
        return None

    root = TreeNode(nodes.pop(0))
    queue = [root]

    while nodes:
        left_val = nodes.pop(0)
        if nodes:
            right_val = nodes.pop(0)
        else:
            right_val = None

        node = queue.pop(0)
        if left_val:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        if right_val:
            node.right = TreeNode(right_val)
            queue.append(node.right)

    return root


def to_list(root: Optional[TreeNode]) -> List[int]:
    """Cria uma lista a partir de uma árvore binária"""
    nodes = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        nodes.append(node.val if node else None)

        if not node:
            continue

        queue.append(node.left)
        queue.append(node.right)

    while not nodes[-1]:
        nodes.pop()

    return nodes


class Solution:
    """Solution"""

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """1372. Longest zigzag path in a binary tree"""
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().longestZigZag,
    ]

    # fmt: off
    data = [
        [[ 1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1, ], 3],
        [[1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4],
        [[1], 0],
    ]
    # fmt: on

    for nodes, expected in data:
        for func in funcs:
            root = to_binary_tree(nodes)
            assert func(root) == expected


if __name__ == "__main__":
    pass
