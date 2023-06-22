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

        def is_mirror(left, right):
            """Is mirror?"""
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return is_mirror(root, root)

    def isSymmetric_bfs(self, root: Optional[TreeNode]) -> bool:
        """BFS"""

        queue = [root, root]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.extend([left.left, right.right, left.right, right.left])

        return True
