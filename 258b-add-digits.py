"""
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Constraints:
    0 <= num <= 231 - 1
"""


class Solution:
    def addDigits_loop(self, num):
        pass

    def addDigits_math(self, num):
        pass

    def addDigits_math_shorter(self, num):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().addDigits_loop,
        Solution().addDigits_math,
        Solution().addDigits_math_shorter,
    ]

    data = [
        (38, 2),
        (0, 0),
    ]

    for num, expected in data:
        for func in funcs:
            assert func(num) == expected
