import collections


class Solution:
    def invertTree_recursive(self, node):
        if not node:
            return None
        right = self.invertTree_recursive(node.right)
        left = self.invertTree_recursive(node.left)
        node.left = right
        node.right = left
        return node

    def invertTree_iterative(self, root):
        if not root:
            return None

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
