"""
You are given an array prices where prices[i] is the price of a given stock
on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many
transactions as you like, but you need to pay the transaction fee for each
transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

Constraints:
   1 <= prices.length <= 5 * 10^4
   1 <= prices[i] < 5 * 10^4
   0 <= fee < 5 * 10^4
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().maxProfit,
    ]

    # fmt: off
    data = [
        ([1, 3, 2, 8, 4, 9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
    ]
    # fmt: on
    for prices, fee, expected in data:
        for func in funcs:
            assert func(prices, fee) == expected
