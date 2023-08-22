"""
Given an integer columnNumber, return its corresponding column title as it
appears in an Excel sheet.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Constraints:
    1 <= columnNumber <= 2^31 - 1
"""


class Solution:
    def convertToTitle(self, col: int) -> str:
        base = ord("A")
        title = ""

        while col:
            title = chr(base + (col - 1) % 26) + title
            col = (col - 1) // 26

        return title


def test_solution():
    """test"""

    funcs = [
        Solution().convertToTitle,
    ]

    # fmt: off
    data = [
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
    ]
    # fmt: on

    for col, expected in data:
        for func in funcs:
            assert func(col) == expected


if __name__ == "__main__":
    pass
