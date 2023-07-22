"""
On an n x n chessboard, a knight starts at the cell (row, column) and
attempts to make exactly k moves. The rows and columns are 0-indexed, so the
top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below.
Each move is two cells in a cardinal direction, then one cell in an
orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves
uniformly at random (even if the piece would go off the chessboard) and moves
there.

The knight continues moving until it has made exactly k moves or has moved
off the chessboard.

Return the probability that the knight remains on the board after it has
stopped moving.

Constraints:
    1 <= n <= 25
    0 <= k <= 100
    0 <= row, column <= n - 1
"""

from itertools import product
from functools import cache


class Solution:
    def knightProbability_bottom_up_dp(
        self, n: int, k: int, initial_row: int, initial_col: int
    ) -> float:
        """
        Bottom-Up Dynamic Programming
        """
        return 0.0

    def knightProbability_bottom_up_dp_optimized(
        self, n: int, k: int, initial_row: int, initial_col: int
    ) -> float:
        """
        Bottom-Up Dynamic Programming - Space Optimized
        """
        return 0.0

    def knightProbability_top_down_dp(
        self, n: int, k: int, initial_row: int, initial_col: int
    ) -> float:
        """
        Top-Down Dynamic Programming
        """
        return 0.0


def test_solution():
    """test"""

    funcs = [
        Solution().knightProbability_bottom_up_dp,
        Solution().knightProbability_bottom_up_dp_optimized,
        Solution().knightProbability_top_down_dp,
    ]

    # fmt: off
    data = [
        (3, 2, 0, 0, 0.06250),
        (1, 0, 0, 0, 1.00000),
    ]
    # fmt: on
    for n, k, row, column, expected in data:
        for func in funcs:
            assert func(n, k, row, column) == expected
