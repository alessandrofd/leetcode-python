"""
You have a pointer at index 0 in an array of size arrLen. At each step, you
can move 1 position to the left, 1 position to the right in the array, or
stay in the same place (The pointer should not be placed outside the array at
any time).

Given two integers steps and arrLen, return the number of ways such that your
pointer is still at index 0 after exactly steps steps. Since the answer may
be too large, return it modulo 10^9 + 7.

Constraints:
    1 <= steps <= 500
    1 <= arrLen <= 10^6
"""

from functools import cache


class Solution:
    def numWays_top_down(self, steps: int, arrLen: int) -> int:
        MOD = int(1e9 + 7)

        # Notice in the constraints that while steps can be up to 500, arrLen
        # can be up to 10^6. However, it is impossible for any call to have a
        # value of i greater than steps. The furthest we can go is by only
        # making moves to the right, but we would run out of moves after steps
        # moves. Thus, we can safely perform arrLen = min(arrLen, steps) before
        # starting the algorithm.

        arrLen = min(arrLen, steps)

        @cache
        def dp(i, remain):
            if remain == 0:
                if i == 0:
                    return 1
                return 0

            left = 0 if i == 0 else dp(i - 1, remain - 1)
            right = 0 if i == arrLen - 1 else dp(i + 1, remain - 1)
            stay = dp(i, remain - 1)

            return (left + right + stay) % MOD

        return dp(0, steps)

    def numWays_bottom_up(self, steps: int, arr_len: int) -> int:
        MOD = int(1e9 + 7)

        arr_len = min(arr_len, steps)

        dp = [[0] * (steps + 1) for _ in range(arr_len)]
        dp[0][0] = 1

        for remain in range(1, steps + 1):
            for i in range(arr_len):
                left = 0 if i == 0 else dp[i - 1][remain - 1]
                right = 0 if i == arr_len - 1 else dp[i + 1][remain - 1]
                stay = dp[i][remain - 1]

                dp[i][remain] = (left + right + stay) % MOD

        return dp[0][steps]

    def numWays_bottom_up_space_optimized(self, steps: int, arr_len: int) -> int:
        MOD = int(1e9 + 7)

        arr_len = min(arr_len, steps)

        prev_dp = [0] * arr_len
        prev_dp[0] = 1

        for remain in range(1, steps + 1):
            dp = [0] * arr_len
            for i in range(arr_len):
                left = 0 if i == 0 else prev_dp[i - 1]
                right = 0 if i == arr_len - 1 else prev_dp[i + 1]
                stay = prev_dp[i]

                dp[i] = (left + right + stay) % MOD

            prev_dp = dp

        return prev_dp[0]


def test_solution():
    """test"""

    funcs = [
        Solution().numWays_top_down,
        Solution().numWays_bottom_up,
        Solution().numWays_bottom_up_space_optimized,
    ]

    # fmt: off
    data = [
        [3, 2, 4],
        [2, 4, 2],
        [4, 2, 8],
    ]
    # fmt: on
    for func in funcs:
        for steps, arr_len, expected in data:
            assert func(steps, arr_len) == expected
