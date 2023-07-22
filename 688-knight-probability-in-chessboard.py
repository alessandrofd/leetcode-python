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
        # fmt: off
        moves = [
            (-2, -1), (-2, 1),
            (-1, 2),  (1, 2),
            (2, -1),  (2, 1),
            (-1, -2), (1, -2),
        ]
        # fmt: on

        dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][initial_row][initial_col] = 1

        for turn in range(1, k + 1):
            for row in range(n):
                for col in range(n):
                    for move_row, move_col in moves:
                        prev_row, prev_col = row - move_row, col - move_col
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            dp[turn][row][col] += dp[turn - 1][prev_row][prev_col]
                    dp[turn][row][col] /= 8

        return sum(dp[k][row][col] for row, col in product(range(n), repeat=2))

    def knightProbability_bottom_up_dp_optimized(
        self, n: int, k: int, initial_row: int, initial_col: int
    ) -> float:
        """
        Bottom-Up Dynamic Programming - Space Optimized
        """
        # fmt: off
        moves = [
            (-2, -1), (-2, 1),
            (-1, 2),  (1, 2),
            (2, -1),  (2, 1),
            (-1, -2), (1, -2),
        ]
        # fmt: on

        prev_dp = [[0.0] * n for _ in range(n)]
        prev_dp[initial_row][initial_col] = 1

        for _ in range(k):
            curr_dp = [[0.0] * n for _ in range(n)]
            for row in range(n):
                for col in range(n):
                    for move_row, move_col in moves:
                        prev_row, prev_col = row - move_row, col - move_col
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            curr_dp[row][col] += prev_dp[prev_row][prev_col]
                    curr_dp[row][col] /= 8
            prev_dp = curr_dp

        return sum(prev_dp[row][col] for row, col in product(range(n), repeat=2))

    def knightProbability_top_down_dp(
        self, n: int, k: int, initial_row: int, initial_col: int
    ) -> float:
        """
        Top-Down Dynamic Programming
        """

        @cache
        def calculate_probability(turn, row, col):
            if turn == 0:
                if row == initial_row and col == initial_col:
                    return 1.0
                else:
                    return 0.0

            # fmt: off
            moves = [
                (-2, -1), (-2, 1),
                (-1, 2),  (1, 2),
                (2, -1),  (2, 1),
                (-1, -2), (1, -2),
            ]
            # fmt: on

            prob = 0
            for move_row, move_col in moves:
                prev_row, prev_col = row - move_row, col - move_col
                if 0 <= prev_row < n and 0 <= prev_col < n:
                    prob += calculate_probability(turn - 1, prev_row, prev_col)
            prob /= 8

            return prob

        result = 0
        for row, col in product(range(n), repeat=2):
            result += calculate_probability(k, row, col)

        return result


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
