"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is
completely filled, and all nodes in the last level are as far left as
possible. It can have between 1 and 2h nodes inclusive at the last level h.

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    1 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def isCompleteTree_BFS(  # pylint: disable=invalid-name
        self, root: Optional[TreeNode]
    ) -> bool:
        """BFS"""

    def isCompleteTree_DFS(  # pylint: disable=invalid-name
        self, root: Optional[TreeNode]
    ) -> bool:
        """DFS"""
