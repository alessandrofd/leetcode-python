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
import collections


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
        count_subtrees = collections.defaultdict(int)
        result = []

        def traverse(node):
            if not node:
                return ""

            subtree = f"(({traverse(node.left)}){node.val}({traverse(node.right)}))"

            count_subtrees[subtree] += 1
            if 2 == count_subtrees[subtree]:
                result.append(node)

            return subtree

        traverse(root)
        return result

    def findDuplicateSubtrees_id(self, root):  # pylint: disable=invalid-name
        """ID representation approach"""
        count_subtrees = collections.defaultdict(int)
        triplet_to_id = {}
        result = []

        def traverse(node):
            if not node:
                return 0

            triplet = (traverse(node.left), node.val, traverse(node.right))

            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            triplet_id = triplet_to_id[triplet]

            count_subtrees[triplet_id] += 1
            if 2 == count_subtrees[triplet_id]:
                result.append(node)

            return id

        traverse(root)
        return result
