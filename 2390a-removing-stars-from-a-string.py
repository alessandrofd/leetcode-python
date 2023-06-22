"""
You are given a string s, which contains stars *.

In one operation, you can:
    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove
    the star itself.
    Return the string after all stars have been removed.

Note:
    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters and stars *.
    The operation above can be performed on s.
"""


class Solution:
    def removeStars(self, string):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().removeStars,
    ]

    data = [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ]

    for string, output in data:
        for func in funcs:
            assert func(string) == output
