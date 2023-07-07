"""
Given the root of a binary tree, the level of its root is 1, the level of its
children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at
level x is maximal.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5
"""

from typing import Optional
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum_dfs(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return
            levels[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        max_val = -float("inf")
        max_level = 0

        for level, val in levels.items():
            if val > max_val:
                max_val = val
                max_level = level

        return max_level

    def maxLevelSum_bfs(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")
        max_level = 0
        level = 0

        queue = deque([root])

        while queue:
            n = len(queue)
            level += 1
            level_sum = 0

            for _ in range(n):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level
