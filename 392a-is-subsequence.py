"""
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return False


def test_solution():
    """test"""

    funcs = [
        Solution().isSubsequence,
    ]

    # fmt: off
    data = [
        ['abc', 'ahbgdc', True],
        ['axc', 'ahbgdc', False],
    ]
    # fmt: on

    for s, t, expected in data:
        for func in funcs:
            assert func(s, t) == expected


if __name__ == "__main__":
    pass
