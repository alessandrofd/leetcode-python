"""
Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

Constraints:
    The number of nodes in the tree is in the range [2, 104].
    0 <= Node.val <= 10^5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = int(1e5)
        prev_node = None

        def inorder_traversal(node):
            nonlocal min_diff, prev_node

            if not node:
                return

            inorder_traversal(node.left)

            if prev_node:
                min_diff = min(min_diff, node.val - prev_node.val)
            prev_node = node

            inorder_traversal(node.right)

        inorder_traversal(root)
        return min_diff
