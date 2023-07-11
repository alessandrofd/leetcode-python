"""
Given two strings s and goal, return true if you can swap two letters in s so
the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such
that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Constraints:
    1 <= s.length, goal.length <= 2 * 10^4
    s and goal consist of lowercase letters.
"""

from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)

        if n == 1:
            return False

        if len(s) != len(goal):
            return False

        if s == goal:
            if len(set(s)) == len(s):
                return False
            return True

        diffs = []
        for a, b in zip(s, goal):
            if a != b:
                if len(diffs) == 2:
                    return False
                diffs.append((a, b))

        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]


def test_solution():
    """test"""

    funcs = [
        Solution().buddyStrings,
    ]

    # fmt: off
    data = [
        ('ab', 'ba', True),
        ('ab', 'ab', False),
        ('aa', 'aa', True),
        ('abcaa', 'abcbb', False),
        ('abac', 'abad', False),
    ]
    # fmt: on
    for s, goal, expected in data:
        for func in funcs:
            assert func(s, goal) == expected
