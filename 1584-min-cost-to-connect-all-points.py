"""
'You are given an array points representing integer coordinates of some points
on a 2D-plane, where points[i] = [xi, yi]

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
absolute value of val.

Return the minimum cost to make all points connected. All points are
connected if there is exactly one simple path between any two points.

Constraints:
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    All pairs (xi, yi) are distinct.
"""

from typing import List
from itertools import product


class Solution:
    def minCostConnectPoints_kruskal(self, points: List[List[int]]) -> int:
        n = len(points)

        if n == 1:
            return 0

        parents = list(range(n))

        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]

        def union(i, j):
            i = find(i)
            j = find(j)

            if i == j:
                return False

            parents[j] = i
            return True

        connections = []
        for i, j in product(range(n), repeat=2):
            xi, yi = points[i]
            xj, yj = points[j]
            cost = abs(xi - xj) + abs(yi - yj)
            connections.append((i, j, cost))

        connections.sort(key=lambda x: x[2])

        count = 0
        result = 0
        for i, j, cost in connections:
            if not union(i, j):
                continue

            result += cost
            count += 1
            if count == n - 1:
                return result

        return -1

    def minCostConnectPoints_prim(self, points: List[List[int]]) -> int:
        # Prim - TLE
        n = len(points)
        unconnected = set(range(n))
        connected = set()

        unconnected.remove(0)
        connected.add(0)
        result = 0

        while len(connected) < n:
            min_cost = 4 * (10**6) + 1
            candidate = -1
            for i in connected:
                xi, yi = points[i]
                for j in unconnected:
                    xj, yj = points[j]
                    cost = abs(xi - xj) + abs(yi - yj)
                    if cost < min_cost:
                        min_cost = cost
                        candidate = j

            result += min_cost
            connected.add(candidate)
            unconnected.remove(candidate)

        return result

    def minCostConnectPoints_prim_cached(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [4_000_001] * n
        connected = set([0])

        last = 0
        result = 0

        while len(connected) < n:
            min_cost = 4_000_001
            candidate = -1
            xi, yi = points[last]
            for current in range(1, n):
                if current in connected:
                    continue

                xj, yj = points[current]
                cost = abs(xi - xj) + abs(yi - yj)
                dist[current] = min(dist[current], cost)

                if dist[current] < min_cost:
                    min_cost = dist[current]
                    candidate = current

            result += min_cost
            connected.add(candidate)
            last = candidate

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().minCostConnectPoints_kruskal,
        Solution().minCostConnectPoints_prim,
        Solution().minCostConnectPoints_prim_cached,
    ]

    data = [
        (
            [
                [0, 0],
                [2, 2],
                [3, 10],
                [5, 2],
                [7, 0],
            ],
            20,
        ),
        (
            [
                [3, 12],
                [-2, 5],
                [-4, 1],
            ],
            18,
        ),
        ([[-1000000, -1000000], [1000000, 1000000]], 4_000_000),
    ]
    for points, expected in data:
        for func in funcs:
            assert func(points) == expected


if __name__ == "__main__":
    pass
