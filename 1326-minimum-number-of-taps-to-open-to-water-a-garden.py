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
        dp = [n + 2] * (n + 1)
        dp[0] = 0

        for i, range_tap in enumerate(ranges):
            start = max(0, i - range_tap)
            end = min(n, i + range_tap)
            for j in range(start, end + 1):
                dp[end] = min(dp[end], dp[j] + 1)

        return -1 if dp[n] == n + 2 else dp[n]

    def minTaps_greedy(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)
        for i, range_tap in enumerate(ranges):
            start = max(0, i - range_tap)
            end = min(n, i + range_tap)
            max_reach[start] = max(max_reach[start], end)

        taps = 0
        curr_end = 0
        next_end = 0
        for i, reach in enumerate(max_reach):
            if i > next_end:
                return -1

            if i > curr_end:
                taps += 1
                curr_end = next_end

            next_end = max(next_end, reach)

        return taps


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
