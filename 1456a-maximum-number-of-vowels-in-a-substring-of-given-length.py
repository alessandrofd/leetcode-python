"""
Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= s.length
"""


class Solution:
    """solution class"""

    def maxVowels(self, input_string: str, window_length: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().maxVowels,
    ]

    data = [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
    ]

    for input_string, window_length, expected in data:
        for func in funcs:
            assert func(input_string, window_length) == expected
