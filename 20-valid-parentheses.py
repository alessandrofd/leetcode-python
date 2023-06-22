"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and 
']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, string):
        symbols = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for symbol in string:
            if symbol in symbols:
                stack.append(symbol)
            else:
                if not stack or symbol != symbols[stack.pop()]:
                    return False

        return not stack


def test_solution():
    """test"""

    funcs = [
        Solution().isValid,
    ]

    data = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("((", False),
        ("]", False),
    ]

    for string, output in data:
        for func in funcs:
            assert func(string) == output
