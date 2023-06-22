"""
There is a biker going on a road trip. The road trip consists of n + 1 points
at different altitudes. The biker starts his trip on point 0 with altitude
equal 0.

You are given an integer array gain of length n where gain[i] is the net gain
in altitude between points i and i + 1 for all (0 <= i < n). Return the
highest altitude of a point.

Constraints:
    n == gain.length
    1 <= n <= 100
    -100 <= gain[i] <= 100
"""
from typing import List
from itertools import accumulate


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, *accumulate(gain))


def test_solution():
    """test"""

    funcs = [
        Solution().largestAltitude,
    ]

    # fmt: off
    data = [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ]
    # fmt: on
    for gain, expected in data:
        for func in funcs:
            assert func(gain) == expected
