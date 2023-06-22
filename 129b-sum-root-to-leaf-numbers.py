"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated
so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def sumNumbers_dfs(self, root):  # pylint: disable=invalid-name
        """DFS"""

    def sumNumbers_bfs(self, root):  # pylint: disable=invalid-name
        """BFS"""

    def sumNumbers_morris(self, root):  # pylint: disable=invalid-name
        """Morris Preorder Traversal"""
