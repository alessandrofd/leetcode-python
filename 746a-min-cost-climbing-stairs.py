"""
You are given an integer array cost where cost[i] is the cost of ith step
on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""

from functools import cache


class Solution:
    def minCostClimbingStairs_dp_top_down(self, cost: list[int]) -> int:
        n = len(cost)

        @cache
        def dp(i):
            if i >= n:
                return 0

            return cost[i] + min(dp(i + 1), dp(i + 2))

        return min(dp(0), dp(1))

    def minCostClimbingStairs_dp_bottom_up(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[n - 1] = cost[n - 1]
        dp[n - 2] = cost[n - 2]

        for i in range(n - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])

    def minCostClimbingStairs_dp_bottom_up_constant_space(self, cost: list[int]) -> int:
        n = len(cost)
        one_step, two_steps = cost[n - 2], cost[n - 1]

        for i in range(n - 3, -1, -1):
            curr = cost[i] + min(one_step, two_steps)
            two_steps, one_step = one_step, curr

        return min(one_step, two_steps)

    def minCostClimbingStairs_dp_bottom_up_no_extra_space(self, cost: list[int]) -> int:
        n = len(cost)

        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


def test_solution():
    """test"""

    funcs = [
        Solution().minCostClimbingStairs_dp_top_down,
        Solution().minCostClimbingStairs_dp_bottom_up,
        Solution().minCostClimbingStairs_dp_bottom_up_constant_space,
        Solution().minCostClimbingStairs_dp_bottom_up_no_extra_space,
    ]

    # fmt: off
    data = [
        [[10, 15, 20], 15],
        [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6],
    ]
    # fmt: on
    for cost, expected in data:
        for func in funcs:
            assert func(cost) == expected
