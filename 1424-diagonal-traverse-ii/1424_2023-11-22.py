from collections import defaultdict, deque


class Solution:
    def findDiagonalOrder(self, nums):
        result = []

        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            result.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, 0))

            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return result

    def findDiagonalOrder_by_diag(self, nums):
        diags = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diag = row + col
                diags[diag].append(nums[row][col])

        result = []
        diag = 0
        while diag in diags:
            result.extend(diags[diag])
            diag += 1

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().findDiagonalOrder,
        Solution().findDiagonalOrder_by_diag,
    ]

    data = [
        [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 4, 2, 7, 5, 3, 8, 6, 9],
        ],
        [
            [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
            [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        ],
    ]

    for func in funcs:
        for nums, expected in data:
            assert func(nums) == expected
