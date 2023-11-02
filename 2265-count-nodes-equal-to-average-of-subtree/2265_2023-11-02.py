class Solution:
    def averageOfSubtree(self, root):
        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return (0, 0)

            sum_left, count_left = dfs(node.left)
            sum_right, count_right = dfs(node.right)
            sum_node = sum_left + sum_right + node.val
            count_node = count_left + count_right + 1

            if sum_node // count_node == node.val:
                result += 1

            return (sum_node, count_node)

        dfs(root)
        return result
