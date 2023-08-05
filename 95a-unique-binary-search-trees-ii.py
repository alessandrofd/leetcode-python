"""
Given an integer n, return all the structurally unique BST's (binary search
trees), which has exactly n nodes of unique values from 1 to n. Return the
answer in any order.

Constraints:
    1 <= n <= 8
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return [None]


if __name__ == "__main__":
    trees = Solution().generateTrees(3)
    print(trees)
