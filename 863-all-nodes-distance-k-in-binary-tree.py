"""
Given the root of a binary tree, the value of a target node target, and
an integer k, return an array of the values of all nodes that have
a distance k from the target node.

You can return the answer in any order.

Constraints:
    The number of nodes in the tree is in the range [1, 500].
    0 <= Node.val <= 500
    All the values Node.val are unique.
    target is the value of one of the nodes in the tree.
    0 <= k <= 1000
"""

from typing import List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return

            if node and parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)

            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        distance = 0
        visited = set()
        queue = deque([target.val])

        while queue:
            if distance == k:
                return list(queue)

            n = len(queue)
            for _ in range(n):
                node = queue.popleft()

                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)

            distance += 1

        return []
