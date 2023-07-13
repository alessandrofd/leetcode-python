"""
You are given an array of characters letters that is sorted in non-decreasing
order, and a character target. There are at least two different characters in
letters.

Return the smallest character in letters that is lexicographically greater
than target. If such a character does not exist, return the first character
n letters.

Constraints:
    2 <= letters.length <= 10^4
    letters[i] is a lowercase English letter.
    letters is sorted in non-decreasing order.
    letters contains at least two different characters.
    target is a lowercase English letter.
"""

from typing import List
from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target) % len(letters)]


def test_solution():
    """test"""

    funcs = [
        Solution().nextGreatestLetter,
    ]

    # fmt: off
    data = [
        (['c', 'f', 'j'], 'a', "c"),
        (['c', 'f', 'j'], 'c', "f"),
        (['x', 'x', 'y', 'y'], 'z', "x"),
    ]
    # fmt: on
    for letters, target, expected in data:
        for func in funcs:
            assert func(letters, target) == expected
