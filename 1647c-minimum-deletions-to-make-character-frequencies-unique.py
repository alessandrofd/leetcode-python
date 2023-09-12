"""
A string s is called good if there are no two different characters in s that
have the same frequency.

Given a string s, return the minimum number of characters you need to delete
to make s good.

The frequency of a character in a string is the number of times it appears in
the string. For example, in the string "aab", the frequency of 'a' is 2,
while the frequency of 'b' is 1.

Constraints:
    1 <= s.length <= 10^5
    s contains only lowercase English letters.
"""

from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def minDeletions_duplicates(self, s):
        """Set"""
        pass

    def minDeletions_priority_queue(self, s):
        """Priority Queue"""
        pass

    def minDeletions_sorting(self, s):
        """Sorting"""
        pass


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().minDeletions_duplicates,
        Solution().minDeletions_priority_queue,
        Solution().minDeletions_sorting,
    ]

    data = [
        ['aab', 0],
        ['aaabbbcc', 2],
        ['ceabaacb', 2],
        ['bbcebab', 2],
        ["abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz", 276],
    ]
    # fmt: on

    for string, expected in data:
        for func in funcs:
            assert func(string) == expected


if __name__ == "__main__":
    pass
