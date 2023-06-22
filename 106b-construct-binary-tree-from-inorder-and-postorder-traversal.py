"""
Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the
same tree, construct and return the binary tree.

Constraints:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.
"""

from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def buildTree_slice(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """Slice"""
        if not inorder:
            return None

        root = postorder[-1]
        index = inorder.index(root)
        return TreeNode(
            root,
            self.buildTree(inorder[:index], postorder[:index]),
            self.buildTree(inorder[index + 1 :], postorder[index:-1]),
        )

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Hash"""

        inorder_hash = {}
        for i, val in enumerate(inorder):
            inorder_hash[val] = i

        nodes = 0

        def recurse(start, end):
            nonlocal nodes

            if start > end:
                return None

            root_val = postorder[-1 - nodes]
            root = TreeNode(root_val)
            nodes += 1

            root_index = inorder_hash[root_val]
            root.right = recurse(root_index + 1, end)
            root.left = recurse(start, root_index - 1)

            return root

        return recurse(0, len(inorder) - 1)
