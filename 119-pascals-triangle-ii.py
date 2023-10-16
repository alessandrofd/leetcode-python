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
        if row_index == 0:
            return [1]
        if row_index == 1:
            return [1, 1]

        prev_row = [1, 1]

        for i in range(1, row_index):
            row = [1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
            prev_row = row

        return prev_row


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
