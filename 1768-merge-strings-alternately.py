"""
You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer than
the other, append the additional letters onto the end of the merged string.

Return the merged string.

Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1, word2):
        merged_word = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            merged_word += word1[i] + word2[i]

        merged_word += word1[min_len:] + word2[min_len:]

        return merged_word


def test_solution():
    """test"""

    funcs = [
        Solution().mergeAlternately,
    ]

    data = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ]

    for word1, word2, output in data:
        for func in funcs:
            assert func(word1, word2) == output
