"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are
divided into n and m substrings respectively, such that:

    s = s1 + s2 + ... + sn

    t = t1 + t2 + ... + tm

    |n - m| <= 1

    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or
    t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.
"""

from collections import Counter
from functools import cache
from itertools import product


class Solution:
    def isInterleave_dp_top_down(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        k = len(s3)

        if m + n != k:
            return False

        if Counter(s1 + s2) != Counter(s3):
            return False

        @cache
        def dfs(i, j):
            if i == m and j == n:
                return True
            return (i < m and s1[i] == s3[i + j] and dfs(i + 1, j)) or (
                j < n and s2[j] == s3[i + j] and dfs(i, j + 1)
            )

        return dfs(0, 0)

    def isInterleave_dp_bottom_up(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        k = len(s3)

        if m + n != k:
            return False

        if Counter(s1 + s2) != Counter(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i, j in product(range(m + 1), range(n + 1)):
            dp[i][j] = (
                dp[i][j]
                or (i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                or (j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            )

        return dp[m][n]


def test_solution():
    """test"""

    funcs = [
        Solution().isInterleave_dp_top_down,
        Solution().isInterleave_dp_bottom_up,
    ]

    # fmt: off
    data = [
        ['aabcc', 'dbbca', 'aadbbcbcac', True],
        ['aabcc', 'dbbca', 'aadbbbaccc', False],
        ['', '', '', True],
        ['a', 'b', 'a', False],
        ['a', '', 'a', True],

    ]
    # fmt: on

    for s1, s2, s3, expected in data:
        for func in funcs:
            assert func(s1, s2, s3) == expected


if __name__ == "__main__":
    pass
