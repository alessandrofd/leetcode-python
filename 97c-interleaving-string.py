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
        return False

    def isInterleave_dp_bottom_up(self, s1: str, s2: str, s3: str) -> bool:
        return False


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
