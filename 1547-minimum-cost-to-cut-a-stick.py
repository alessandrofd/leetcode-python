"""
Given a wooden stick of length n units. The stick is labelled from 0 to n.
For example, a stick of length 6 is labelled as follows:

Given an integer array cuts where cuts[i] denotes a position you should
perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as
you wish.

The cost of one cut is the length of the stick to be cut, the total cost is
the sum of costs of all cuts. When you cut a stick, it will be split into two
smaller sticks (i.e. the sum of their lengths is the length of the stick
before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

Constraints:
    2 <= n <= 10^6
    1 <= cuts.length <= min(n - 1, 100)
    1 <= cuts[i] <= n - 1
    All the integers in cuts array are distinct.
"""
from typing import List
from functools import cache

# Ao invés de considerarmos cada fragmento individual, nós os agrupamos pelos
# cortes, já que fragmentos sem cortes são inócuos para a resolução do problema


class Solution:
    def minCost_dp(self, n: int, cuts: List[int]) -> int:
        frags = sorted([0] + list(cuts) + [n])
        m = len(frags)

        dp = [[0] * m for i in range(m)]

        for diff in range(2, m):
            for left in range(m - diff):
                right = left + diff
                cost = int(1e8)
                for cut in range(left + 1, right):
                    cost = min(cost, dp[left][cut] + dp[cut][right])

                dp[left][right] = cost + (frags[right] - frags[left])

        return dp[0][m - 1]

    def minCost_recursion(self, n: int, cuts: List[int]) -> int:
        frags = sorted([0] + list(cuts) + [n])
        m = len(frags)

        @cache
        def f(left, right):
            if right - left == 1:
                return 0

            cost = 1e8
            for cut in range(left + 1, right):
                cost = min(cost, f(left, cut) + f(cut, right))

            return cost + (frags[right] - frags[left])

        return f(0, m - 1)


def test_solution():
    """test"""

    funcs = [
        Solution().minCost_dp,
        Solution().minCost_recursion,
    ]

    data = [
        (7, [1, 3, 4, 5], 16),
        (9, [5, 6, 1, 4, 2], 22),
        (
            3829,
            [
                3689,
                2882,
                1725,
                1655,
                1495,
                2988,
                1993,
                1550,
                2575,
                1510,
                1370,
                2558,
                1890,
                3580,
                434,
                3589,
                601,
                396,
                3745,
                2961,
                229,
                2275,
                3559,
                952,
                2677,
                682,
            ],
            16649,
        ),
    ]
    for n, cuts, expected in data:
        for func in funcs:
            assert func(n, cuts) == expected
