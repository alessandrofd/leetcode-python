"""
Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.
 *
Constraints:
    1 <= s.length <= 5 * 10^4
    s contains printable ASCII characters.
    s does not contain any leading or trailing spaces.
    There is at least one word in s.
    All the words in s are separated by a single space
"""


class Solution:
    def reverseWords(self, sentence: str) -> str:
        return ""


def test_solution():
    """test"""

    funcs = [
        Solution().reverseWords,
    ]

    # fmt: off
    data = [
        ["Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"],
        ['God Ding', 'doG gniD'],
    ]
    # fmt: on
    for sentence, expected in data:
        for func in funcs:
            assert func(sentence) == expected
