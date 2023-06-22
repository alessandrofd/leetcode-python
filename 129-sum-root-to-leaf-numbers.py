"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated
so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def sumNumbers_dfs(self, root):  # pylint: disable=invalid-name
        """DFS"""

        sum_nums = 0

        def recurse(node, num):
            nonlocal sum_nums

            if not node:
                return

            num = num * 10 + node.val
            if not (node.left or node.right):
                sum_nums += num

            recurse(node.left, num)
            recurse(node.right, num)

        recurse(root, 0)
        return sum_nums

    def sumNumbers_bfs(self, root):  # pylint: disable=invalid-name
        """BFS"""
        sum_nums = 0

        queue = [(root, 0)]
        while queue:
            node, num = queue.pop(0)
            if not node:
                continue

            num = num * 10 + node.val
            if not (node.left or node.right):
                sum_nums += num

            queue.append((node.left, num))
            queue.append((node.right, num))

        return sum_nums

    def sumNumbers_morris(self, root):  # pylint: disable=invalid-name
        """Morris Preorder Traversal"""

        sum_nums = 0
        num = 0
        steps = 0

        while root:
            if root.left:
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                    steps += 1

                if not predecessor.right:
                    num = num * 10 + root.val

                    predecessor.right = root
                    root = root.left
                else:
                    if not predecessor.left:
                        sum_nums += num

                    num = num // 10**steps

                    predecessor.right = None
                    root = root.right
            else:
                num = num * 10 + root.val

                if not root.right:
                    sum_nums += num

                root = root.right

        return sum_nums
