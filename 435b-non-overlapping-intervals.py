"""
 * Given an array of intervals intervals where intervals[i] = [starti, endi],
 * return the minimum number of intervals you need to remove to make the rest of
 * the intervals non-overlapping.
 *
 * Constraints:
 *    1 <= intervals.length <= 10^5
 *    intervals[i].length == 2
 *    -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List

# Greedy


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().eraseOverlapIntervals,
    ]

    # fmt: off
    data = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
    ]
    # fmt: on
    for intervals, expected in data:
        for func in funcs:
            assert func(intervals) == expected
