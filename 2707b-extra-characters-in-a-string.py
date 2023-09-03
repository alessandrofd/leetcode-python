"""
You are given a 0-indexed string s and a dictionary of words dictionary. You
have to break s into one or more non-overlapping substrings such that each
substring is present in dictionary. There may be some extra characters in s
which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s
optimally.

Constraints:
    1 <= s.length <= 50
    1 <= dictionary.length <= 50Kw
    1 <= dictionary[i].length <= 50
    dictionary[i] and s consists of only lowercase English letters
    dictionary contains distinct words
"""

from typing import List
from functools import cache


class Solution:
    def minExtraChar_dp_top_down(self, s: str, dictionary: List[str]) -> int:
        """DP Top-Down Substring"""

        return 0

    def minExtraChar_dp_bottom_up(self, s: str, dictionary: List[str]) -> int:
        """DP Bottom-Up Substring"""

        return 0

    def minExtraChar_dp_top_down_trie(self, s: str, dictionary: List[str]) -> int:
        """DP Top-Down Trie"""

        return 0

    def minExtraChar_dp_bottom_up_trie(self, s: str, dictionary: List[str]) -> int:
        """DP Bottom-Up Trie"""

        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().minExtraChar_dp_top_down,
        Solution().minExtraChar_dp_bottom_up,
        Solution().minExtraChar_dp_top_down_trie,
        Solution().minExtraChar_dp_bottom_up_trie,
    ]

    data = [
        ["leetscode", ["leet", "code", "leetcode"], 1],
        ["sayhelloworld", ["hello", "world"], 3],
    ]

    for s, dicitionary, expected in data:
        for func in funcs:
            assert func(s, dicitionary) == expected
