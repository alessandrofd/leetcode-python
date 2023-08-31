"""
There is a one-dimensional garden on the x-axis. The garden starts at the
point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where
ranges[i] (0-indexed) means the i-th tap can water the area
[i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole
garden, If the garden cannot be watered return -1.

Constraints:
    1 <= n <= 10^4
    ranges.length == n + 1
    0 <= ranges[i] <= 100
"""

from typing import List


class Solution:
    def minTaps_dp(self, n: int, ranges: List[int]) -> int:
        return -1

    def minTaps_greedy(self, n: int, ranges: List[int]) -> int:
        return -1


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().minTaps_dp,
        Solution().minTaps_greedy
    ]


    data = [
        [5, [3, 4, 1, 1, 0, 0], 1],
        [3, [0, 0, 0, 0], -1],
        [7, [1, 2, 1, 0, 2, 1, 0, 1], 3],
        [
            35,
            [
            1, 0, 4, 0, 4, 1, 4, 3, 1, 1, 1, 2, 1, 4, 0, 3, 0, 3, 0, 3, 0, 5, 3, 0, 0,
            1, 2, 1, 2, 4, 3, 0, 1, 0, 5, 2,
            ],
            6,
        ],
    ]
    # fmt: on

    for n, ranges, expected in data:
        for func in funcs:
            assert func(n, ranges) == expected


if __name__ == "__main__":
    pass
