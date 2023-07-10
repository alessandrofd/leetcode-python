"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [0, 10^5].
    -1000 <= Node.val <= 1000
"""

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            depth += 1
            for i in range(n):
                node = queue.popleft()
                if not node:
                    continue

                if not (node.left or node.right):
                    return depth

                queue.append(node.left)
                queue.append(node.right)

        return depth
