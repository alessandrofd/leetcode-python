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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root):
        longest_path = 0

        def dfs(node, direction):
            nonlocal longest_path

            if node is None:
                return 0

            left_path = dfs(node.left, "left")
            right_path = dfs(node.right, "right")

            longest_path = max(longest_path, left_path, right_path)

            if direction == "left":
                return right_path + 1
            else:
                return left_path + 1

        dfs(root, "")
        return longest_path
