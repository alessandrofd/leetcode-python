from collections import defaultdict


class Solution:
    def findMode_dfs_iterative(self, root):
        counter = defaultdict(int)

        stack = [root]
        while stack:
            node = stack.pop()
            counter[node.val] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        result = []
        max_count = max(counter.values())
        for val, count in counter.items():
            if count == max_count:
                result.append(val)

        return result

    def findMode_no_map(self, root):
        values = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            values.append(node.val)

            dfs(node.right)

        curr_streak = 0
        max_streak = 0
        curr_num = 0
        result = []

        for num in values:
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                max_streak = curr_streak
                result = []

            if curr_streak == max_streak:
                result.append(num)

        return result

    def findMode_no_map_constant_space(self, root):
        curr_streak = 0
        max_streak = 0
        curr_num = 0
        result = []

        def dfs(node):
            nonlocal curr_streak, max_streak, curr_num, result

            if not node:
                return

            dfs(node.left)

            num = node.val

            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                max_streak = curr_streak
                result = []

            if curr_streak == max_streak:
                result.append(num)

            dfs(node.right)

        dfs(root)
        return result

    def findMode(self, root):
        curr_streak = 0
        max_streak = 0
        curr_num = 0
        result = []

        curr = root
        while curr:
            if curr.left:
                # Find friend and connect it to curr
                friend = curr.left
                while friend.right:
                    friend = friend.right
                friend.right = curr

                # Move to curr.left and delete the edge
                left = curr.left
                curr.left = None
                curr = left
            else:
                num = curr.val

                if num == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num

                if curr_streak > max_streak:
                    max_streak = curr_streak
                    result = []

                if curr_streak == max_streak:
                    result.append(num)

                curr = curr.right

        return result
