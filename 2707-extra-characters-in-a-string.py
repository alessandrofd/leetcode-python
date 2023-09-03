"""
You are given a 0-indexed string s and a dictionary of words dictionary. You
have to break s into one or more non-overlapping substrings such that each
substring is present in dictionary. There may be some extra characters in s
which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s
optimally.

Constraints:
    1 <= s.length <= 50
    1 <= dictionary.length <= 50
    1 <= dictionary[i].length <= 50
    dictionary[i] and s consists of only lowercase English letters
    dictionary contains distinct words
"""

from typing import List
from functools import cache


class Solution:
    def minExtraChar_dp_top_down(self, s: str, dictionary: List[str]) -> int:
        """DP Top-Down Substring"""
        n = len(s)
        word_set = set(dictionary)

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0

            result = dfs(i + 1) + 1
            for j in range(i, n):
                if s[i : j + 1] in word_set:
                    result = min(result, dfs(j + 1))

            return result

        return dfs(0)

    def minExtraChar_dp_bottom_up(self, s: str, dictionary: List[str]) -> int:
        """DP Bottom-Up Substring"""
        n = len(s)
        word_set = set(dictionary)

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i, n):
                if s[i : j + 1] in word_set:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]

    def minExtraChar_dp_top_down_trie(self, s: str, dictionary: List[str]) -> int:
        """DP Top-Down Trie"""
        n = len(s)
        trie = build_trie(dictionary)

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0

            result = dfs(i + 1) + 1
            node = trie
            for j in range(i, n):
                if s[j] not in node.children:
                    break

                node = node.children[s[j]]
                if node.is_word:
                    result = min(result, dfs(j + 1))

            return result

        return dfs(0)

    def minExtraChar_dp_bottom_up_trie(self, s: str, dictionary: List[str]) -> int:
        """DP Bottom-Up Trie"""
        n = len(s)
        trie = build_trie(dictionary)

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            node = trie
            for j in range(i, n):
                if s[j] not in node.children:
                    break

                node = node.children[s[j]]
                if node.is_word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def build_trie(dictionary):
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    return root


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
