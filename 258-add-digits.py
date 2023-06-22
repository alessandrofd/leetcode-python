"""
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Constraints:
    0 <= num <= 231 - 1
"""


class Solution:
    def addDigits_loop(self, num):
        while num >= 10:
            num = sum(int(c) for c in str(num))
        return num

    def addDigits_math(self, num):
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

    def addDigits_math_shorter(self, num):
        return 0 if num == 0 else 1 + ((num - 1) % 9)


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
