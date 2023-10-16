"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it.

Constraints:
    0 <= rowIndex <= 33
"""


class Solution:
    def getRow(self, row_index: int) -> list[int]:
        return []


def test_solution():
    """test"""

    funcs = [
        Solution().getRow,
    ]

    # fmt: off
    data = [
        [3, [1, 3, 3, 1]],
        [0, [1]],
        [1, [1, 1]],
    ]
    # fmt: on
    for func in funcs:
        for row_index, expected in data:
            assert func(row_index) == expected
