"""
We define the usage of capitals in a word to be right when one of the
following cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Given a string word, return true if the usage of capitals in it is right.

Constraints:
    1 <= word.length <= 100
    word consists of lowercase and uppercase English letters.
"""
import re


class Solution:
    def detectCapitalUse_whole_word(self, word: str) -> bool:
        if len(word) == 1 or word.isupper() or word.islower() or word[1:].islower():
            return True
        return False

    def detectCapitalUse_character(self, word: str) -> bool:
        if len(word) == 1:
            return True

        start = 0 if word[0].islower() else 1
        right_case = word[start].islower()

        for i in range(start + 1, len(word)):
            if word[i].islower() != right_case:
                return False

        return True

    def detectCapitalUse_regex(self, word: str) -> bool:
        return bool(re.fullmatch(r"^[A-Z]+$|^[A-Z]?[a-z]+$", word))


def test_solution():
    """test"""

    funcs = [
        Solution().detectCapitalUse_whole_word,
        Solution().detectCapitalUse_character,
        Solution().detectCapitalUse_regex,
    ]

    # fmt: off
    data = [
        ('USA', True),
        ('FlaG', False),
        ('Leetcode', True),
        ('g', True),
    ]
    # fmt: on
    for word, expected in data:
        for func in funcs:
            assert func(word) == expected
