"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of
any one of them.

Two trees are duplicate if they have the same structure with the same
node values.

Constraints:
The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
"""


class TreeNode:
    """TreeNode class"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def findDuplicateSubtrees_string(self, root):  # pylint: disable=invalid-name
        """String representation approach"""

    def findDuplicateSubtrees_id(self, root):  # pylint: disable=invalid-name
        """ID representation approach"""
