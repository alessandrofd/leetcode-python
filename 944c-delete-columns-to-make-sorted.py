"""
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a
grid.

For example, strs = ["abc", "bce", "cae"] can be arranged as:
    abc
    bce
    cae

You want to delete the columns that are not sorted lexicographically. In the
above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e')
are sorted while column 1 ('b', 'c', 'a') is not, so you would delete
column 1.

Return the number of columns that you will delete.

Constraints:
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 1000
    strs[i] consists of lowercase English letters.
"""

from typing import List


class Solution:
    def minDeletionSize_traverse(self, strs: List[str]) -> int:
        deletes = 0

        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    deletes += 1
                    break
        return deletes

    def minDeletionSize_zip(self, strs: List[str]) -> int:
        return sum(list(row) != sorted(row) for row in zip(*strs))


def test_solution():
    """test"""

    funcs = [
        Solution().minDeletionSize_traverse,
        Solution().minDeletionSize_zip,
    ]

    # fmt: off
    data = [
        (['cba', 'daf', 'ghi'], 1),
        (['a', 'b'], 0),
        (['zyx', 'wvu', 'tsr'], 3),
    ]
    # fmt: on

    for connections, expected in data:
        for func in funcs:
            assert func(connections) == expected
