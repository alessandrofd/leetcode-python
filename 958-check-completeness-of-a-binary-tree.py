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

        null_found = False
        queue = [root]
        while queue:
            if node := queue.pop(0):
                if null_found:
                    return False
                queue.extend([node.left, node.right])
            else:
                null_found = True

        return True

    def isCompleteTree(  # pylint: disable=invalid-name
        self, root: Optional[TreeNode]
    ) -> bool:
        """DFS"""

        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        num_nodes = count_nodes(root)

        def dfs(node, node_index):
            if not node:
                return True

            if node_index >= num_nodes:
                return False

            return dfs(node.left, 2 * node_index + 1) and dfs(
                node.right, 2 * node_index + 2
            )

        return dfs(root, 0)
