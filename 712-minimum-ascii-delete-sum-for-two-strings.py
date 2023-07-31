"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted
characters to make two strings equal.

Constraints:
    1 <= s1.length, s2.length <= 1000
    s1 and s2 consist of lowercase English letters.

OBS: O problema "583. Delete operations for two string" descreve a base da
resolução deste problema.
"""

from functools import cache
from itertools import product


class Solution:
    def minimumDeleteSum_top_down_dp(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        @cache
        def solve(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return 0

            if i == 0:
                return ord(s2[j - 1]) + solve(0, j - 1)

            if j == 0:
                return ord(s1[i - 1]) + solve(i - 1, 0)

            if s1[i - 1] == s2[j - 1]:
                return solve(i - 1, j - 1)

            return min(
                ord(s1[i - 1]) + solve(i - 1, j), ord(s2[j - 1]) + solve(i, j - 1)
            )

        return solve(m, n)

    def minimumDeleteSum_bottom_up_dp(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = ord(s1[i - 1]) + dp[i - 1][0]
        for j in range(1, n + 1):
            dp[0][j] = ord(s2[j - 1]) + dp[0][j - 1]

        for i, j in product(range(1, m + 1), range(1, n + 1)):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1]
                )

        return dp[m][n]

    def minimumDeleteSum_bottom_up_1D_dp(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp_last = [0] * (n + 1)
        for j in range(1, n + 1):
            dp_last[j] = ord(s2[j - 1]) + dp_last[j - 1]

        for i in range(1, m + 1):
            dp_current = [0] * (n + 1)
            dp_current[0] = ord(s1[i - 1]) + dp_last[0]

            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp_current[j] = dp_last[j - 1]
                else:
                    dp_current[j] = min(
                        ord(s1[i - 1]) + dp_last[j], ord(s2[j - 1]) + dp_current[j - 1]
                    )

            dp_last = dp_current

        return dp_last[n]


def test_solution():
    """test"""

    funcs = [
        Solution().minimumDeleteSum_top_down_dp,
        Solution().minimumDeleteSum_bottom_up_dp,
        Solution().minimumDeleteSum_bottom_up_1D_dp,
    ]

    # fmt: off
    data = [
        ('sea', 'eat', 231),
        ('delete', 'leet', 403),
    ]
    # fmt: on
    for word1, word2, expected in data:
        for func in funcs:
            assert func(word1, word2) == expected


if __name__ == "__main__":
    pass
