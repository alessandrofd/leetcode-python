"""
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
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

    def isSymmetric_dfs(self, root: Optional[TreeNode]) -> bool:
        """DFS"""

    def isSymmetric_bfs(self, root: Optional[TreeNode]) -> bool:
        """BFS"""
