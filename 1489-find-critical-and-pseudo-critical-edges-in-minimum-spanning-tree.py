"""
Given a weighted undirected connected graph with n vertices numbered from 0
to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a
bidirectional and weighted edge between nodes ai and bi. A minimum spanning
ree (MST) is a subset of the graph's edges that connects all vertices without
cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum
spanning tree (MST). An MST edge whose deletion from the graph would cause
the MST weight to increase is called a critical edge. On the other hand, a
pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Constraints:
    2 <= n <= 100
    1 <= edges.length <= min(200, n * (n - 1) / 2)
    edges[i].length == 3
    0 <= ai < bi < n
    1 <= weighti <= 1000
    All pairs (ai, bi) are distinct.
"""

from typing import List


class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.components = n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return False

        self.parents[j] = i
        self.components -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        """
        Kruskal
        """
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        std_dsu = DSU(n)
        std_weight = 0
        for u, v, w, _ in edges:
            if not std_dsu.union(u, v):
                continue
            std_weight += w
            if std_dsu.components == 1:
                break

        critical = []
        pseudo = []

        for ui, vi, wi, i in edges:
            critical_dsu = DSU(n)
            critical_weight = 0

            for uj, vj, wj, j in edges:
                if i == j or not critical_dsu.union(uj, vj):
                    continue
                critical_weight += wj
                if critical_dsu.components == 1:
                    break

            if critical_dsu.components > 1 or critical_weight > std_weight:
                critical.append(i)
                continue

            pseudo_dsu = DSU(n)
            pseudo_dsu.union(ui, vi)
            pseudo_weight = wi

            for uj, vj, wj, j in edges:
                if i == j or not pseudo_dsu.union(uj, vj):
                    continue

                pseudo_weight += wj
                if pseudo_dsu.components == 1:
                    break

            if pseudo_dsu.components == 1 and pseudo_weight == std_weight:
                pseudo.append(i)

        return [critical, pseudo]


def test_solution():
    """test"""

    funcs = [
        Solution().findCriticalAndPseudoCriticalEdges,
    ]

    data = [
        (
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
            [[0, 1], [2, 3, 4, 5]],
        ),
        (
            4,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 1],
                [0, 3, 1],
            ],
            [[], [0, 1, 2, 3]],
        ),
    ]
    for n, edges, expected in data:
        for func in funcs:
            assert func(n, edges) == expected


if __name__ == "__main__":
    pass
