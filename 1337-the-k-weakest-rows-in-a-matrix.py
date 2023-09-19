"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and
0's (representing civilians). The soldiers are positioned in front of the
civilians. That is, all the 1's will appear to the left of all the 0's in
each row.

A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in
    row j.

    Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest
to strongest.

Constraints:
    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.
"""

from typing import List


class Solution:
    def kWeakestRows(self, matrix: List[List[int]], num_weakest_rows: int) -> List[int]:
        weakest_rows = [(sum(row), i) for i, row in enumerate(matrix)]
        weakest_rows.sort()
        return [i for _, i in weakest_rows[0:num_weakest_rows]]


def test_solution():
    """test"""

    funcs = [
        Solution().kWeakestRows,
    ]

    # fmt: off
    data = [
        [
            [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
            ],
            3,
            [2, 0, 3],
        ],

        [
            [
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            ],
            2,
            [0, 2],
        ],
    ]
    # fmt: on

    for matrix, num_weakest_rows, expected in data:
        for func in funcs:
            assert func(matrix, num_weakest_rows) == expected


if __name__ == "__main__":
    pass
