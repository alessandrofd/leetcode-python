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
        return 0

    def minimumDeleteSum_bottom_up_dp(self, s1: str, s2: str) -> int:
        return 0

    def minimumDeleteSum_bottom_up_1D_dp(self, s1: str, s2: str) -> int:
        return 0


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
