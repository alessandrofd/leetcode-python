class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            queue_len = len(queue)
            max_val = float("-inf")
            for _ in range(queue_len):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result
