"""
There are some spherical balloons taped onto a flat wall that represents the
XY-plane. The balloons are represented as a 2D integer array points where
points[i] = [xstart, xend] denotes a balloon whose horizontal diameter
stretches between xstart and xend. You do not know the exact y-coordinates of
the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from
different points along the x-axis. A balloon with xstart and xend is burst by
an arrow shot at x if xstart <= x <= xend. There is no limit to the number
of arrows that can be shot. A shot arrow keeps traveling up infinitely,
bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot
to burst all balloons.

Constraints:
    1 <= points.length <= 10^5
    points[i].length == 2
    -2^31 <= xstart < xend <= 2^31 - 1
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 0

        end = points[0][1]
        for next_start, next_end in points[1:]:
            if next_start > end:
                arrows += 1
                end = next_end

        return arrows + 1


def test_solution():
    """test"""

    funcs = [
        Solution().findMinArrowShots,
    ]

    # fmt: off
    data = [
        ([ [10, 16], [2, 8], [1, 6], [7, 12], ], 2),
        ([ [1, 2], [3, 4], [5, 6], [7, 8], ], 4),
        ([ [1, 2], [2, 3], [3, 4], [4, 5], ], 2),
    ]
    # fmt: on
    for points, expected in data:
        for func in funcs:
            assert func(points) == expected
