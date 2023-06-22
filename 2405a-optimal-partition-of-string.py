"""
Given a string s, partition the string into one or more substrings such that
the characters in each substring are unique. That is, no letter appears in
a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in
a partition.

Constraints:
    1 <= s.length <= 10^5
    s consists of only English lowercase letters.
"""


class Solution:
    def partitionString(self, s):


def test_solution():
    """test"""

    funcs = [Solution().partitionString]

    data = [
        ("abacaba", 4),
        ("ssssss", 6),
    ]

    for s, output in data:
        for func in funcs:
            assert func(s) == output
