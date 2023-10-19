"""
Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(string):
            result = []
            for c in string:
                if c == "#":
                    if result:
                        result.pop()
                else:
                    result.append(c)

            return "".join(result)

        return backspace(s) == backspace(t)


def test_solution():
    """test"""

    funcs = [
        Solution().backspaceCompare,
    ]

    # fmt: off
    data = [
        ['ab#c', 'ad#c', True],
        ['ab##', 'c#d#', True],
        ['a#c', 'b', False],
    ]
    # fmt: on
    for func in funcs:
        for s, t, expected in data:
            assert func(s, t) == expected
