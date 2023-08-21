"""
Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""

import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return False if re.match(r"^(.*)\1+$", s) == None else True


def test_solution():
    """test"""

    funcs = [
        Solution().repeatedSubstringPattern,
    ]

    # fmt: off
    data = [
        ('abab', True),
        ('aba', False),
        ('abcabcabcabc', True),
    ]
    # fmt: on
    for s, expected in data:
        for func in funcs:
            assert func(s) == expected


if __name__ == "__main__":
    pass
