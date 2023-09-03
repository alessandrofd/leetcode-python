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


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return 0


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
