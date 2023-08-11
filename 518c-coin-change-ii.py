"""
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount
of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().change,
    ]

    # fmt: off
    data = [
        (5, [1, 2, 5], 4),
        (3, [2], 0),
        (100, [3, 5, 7, 8, 9, 10, 11], 6606),
        (5000, [102, 89, 76, 63, 50, 37, 24, 11], 992951208),
    ]
    # fmt: on
    for amount, coins, expected in data:
        for func in funcs:
            assert func(amount, coins) == expected


if __name__ == "__main__":
    pass
