"""
There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
10^9.
"""

from itertools import product


class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        dp = [[1] * cols for _ in range(rows)]

        for row, col in product(range(1, rows), range(1, cols)):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[rows - 1][cols - 1]


def test_solution():
    """test"""

    funcs = [
        Solution().uniquePaths,
    ]

    data = [
        [3, 7, 28],
        [3, 2, 3],
    ]

    for m, n, expected in data:
        for func in funcs:
            assert func(m, n) == expected
