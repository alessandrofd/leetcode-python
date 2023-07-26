"""
You are given a floating-point number hour, representing the amount of time
you have to reach the office. To commute to the office, you must take
n trains in sequential order. You are also given an integer array dist of
length n, where dist[i] describes the distance (in kilometers) of the ith
train ride.

Each train can only depart at an integer hour, so you may need to wait in
between each train ride.

    For example, if the 1st train ride takes 1.5 hours, you must wait for
    an additional 0.5 hours before you can depart on the 2nd train ride at
    the 2 hour mark.

Return the minimum positive integer speed (in kilometers per hour) that all
the trains must travel at for you to reach the office on time, or -1 if it is
impossible to be on time.

Tests are generated such that the answer will not exceed 10^7 and hour will
have at most two digits after the decimal point.

Constraints:
    n == dist.length
    1 <= n <= 10^5
    1 <= dist[i] <= 10^5
    1 <= hour <= 10^9
    There will be at most two digits after the decimal point in hour.
"""
from typing import List
from math import floor, ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().minSpeedOnTime,
    ]

    # fmt: off
    data = [
        ([1, 3, 2], 6, 1),
        ([1, 3, 2], 2.7, 3),
        ([1, 3, 2], 1.9, -1),
        ([1, 1, 100000], 2.01, 10000000),
        ([5, 3, 4, 6, 2, 2, 7], 10.92, 4),
        ([1, 1], 1.0, -1),
        ([69], 4.6, 15),
        ([6,10,5,1,8,9,2], 34.0, 2),
        ([2, 1, 5, 4, 4, 3, 2, 9, 2, 10], 75.12, 1),
    ]
    # fmt: on
    for dist, hour, expected in data:
        for func in funcs:
            assert func(dist, hour) == expected
