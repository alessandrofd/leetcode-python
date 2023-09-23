"""
You are given an array of words where each word consists of lowercase English
letters.

wordA is a predecessor of wordB if and only if we can insert exactly one
letter anywhere in wordA without changing the order of the other characters
to make it equal to wordB.

    For example, "abc" is a predecessor of "abac", while "cba" is not a
    predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
where word1 is a predecessor of word2, word2 is a predecessor of word3,
and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from
the given list of words.

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of lowercase English letters.
"""


class Solution:
    def longestStrChain_top_down_dp(self, words: list[str]) -> int:
        """Approach 1: Top-Down Dynamic Programming (Recursion + Memoization)"""

        return 0

    def longestStrChain_bottom_up_dp(self, words: list[str]) -> int:
        """Approach 2: Bottom-Up Dynamic Programming"""

        return 0


def test_solution():
    """test"""

    funcs = [
        # Solution().longestStrChain_top_down_dp,
        Solution().longestStrChain_bottom_up_dp,
    ]

    # fmt: off
    data = [
        [['bdca', 'a', 'b', 'ba', 'bca', 'bda'], 4],
        [['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc'], 5],
        [['abcd', 'dbqca'], 1],
    ]
    # fmt: on

    for words, expected in data:
        for func in funcs:
            assert func(words) == expected


if __name__ == "__main__":
    pass
