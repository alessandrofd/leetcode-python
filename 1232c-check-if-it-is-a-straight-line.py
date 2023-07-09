"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
represents the coordinate of a point. Check if these points make a straight
line in the XY plane.

Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""

# Cuidado com o caso em que deltaY = 0 Infinity !== -Infinity

# Ao invés de comparar a inclinação (deltaX / deltaY) é melhor comparar
# os componentes deltaX0 * deltaY1 === deltaX1 * deltaY0


from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return True


def test_solution():
    """test"""

    funcs = [
        Solution().checkStraightLine,
    ]

    # fmt: off
    data = [
        ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True),
        ([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False),
        ([[1,2],[1,3],[1,4],[1,5],[1,6],[6,7]], False),
        ([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]], True),
    ]
    # fmt: on
    for coordinates, expected in data:
        for func in funcs:
            assert func(coordinates) == expected
