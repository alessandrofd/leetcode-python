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
        n = len(coordinates)

        if n == 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0

        for xi, yi in coordinates[2:]:
            if dx * (yi - y0) != dy * (xi - x0):
                return False

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
