"""
Given a string s, remove duplicate letters so that every letter appears once
and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return ""


def test_solution():
    """test"""

    funcs = [
        Solution().removeDuplicateLetters,
    ]

    # fmt: off
    data = [
        ['bcabc', 'abc'],
        ['cbacdcbc', 'acdb'],
        ['leetcode', 'letcod'],
        ['bbcaac', 'bac'],
    ]
    # fmt: on

    for s, expected in data:
        for func in funcs:
            assert func(s) == expected


if __name__ == "__main__":
    pass
