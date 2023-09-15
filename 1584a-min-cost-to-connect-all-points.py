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


class Solution:
    def minCostConnectPoints_kruskal(self, points: List[List[int]]) -> int:
        """Aplicação do algoritmo de Kruskal"""
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

        edges = []
        for i in range(n - 1):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                edges.append([distance, i, j])

        edges.sort()

        result = 0
        count = 0
        for distance, i, j in edges:
            if not union(i, j):
                continue

            result += distance
            count += 1
            if count == n - 1:
                break

        return result

    def minCostConnectPoints_prim(self, points: List[List[int]]) -> int:
        """
        Aplicação do algoritmo de Prim -

        The algorithm starts with an empty spanning tree. The idea is to maintain two
        sets of vertices. The first set contains the vertices already included in the
        MST, and the other set contains the vertices not yet included. At every step,
        it considers all the edges that connect the two sets and picks the minimum
        weight edge from these edges. After picking the edge, it moves the other
        endpoint of the edge to the set containing MST.
        """
        n = len(points)
        if n == 1:
            return 0

        unconnected = set(range(1, n))
        connected = {0}

        result = 0
        while unconnected:
            min_distance = 4_000_001
            closest_point = -1

            for i in connected:
                xi, yi = points[i]
                for j in unconnected:
                    xj, yj = points[j]
                    distance = abs(xi - xj) + abs(yi - yj)
                    if distance < min_distance:
                        min_distance = distance
                        closest_point = j

            unconnected.remove(closest_point)
            connected.add(closest_point)
            result += min_distance

        return result

    def minCostConnectPoints_prim_cached(self, points: List[List[int]]) -> int:
        """
        Aplicação do algoritmo de Prim com as distâncias cacheadas. Escolhemos
        arbitrariament um nó, no nosso caso 0, para iniciar a árvore. Percorremos
        todos os outros nós e calculamos a distância entre eles e a árvore. Esta é
        uma distinção importante, calculamos, e armazenamos, a menor distância entre
        um nó desconectado e a árvore e não a distância entre nós. Isto torna
        desnecessário um laço entre os nós conectados e outro entre os desconectados.
        Basta que calculemos a distância entre o último nó a se conectar à árvore e
        cada um dos nós ainda desconectados. Caso a nova distância seja menor que a
        distância calculada anteriormente, passamos a considerá-lo como a distância
        entre o nó e a árvore. O nó mais próximo da árvore passa a ser o último nó
        conectado à árvore. Repetimos estes passos até que não haja mais nós
        desconectados.
        """
        n = len(points)
        if n == 1:
            return 0

        distances = [4_000_001] * n
        unconnected = set(range(1, n))
        last_connected = 0

        result = 0

        while unconnected:
            min_distance = 4_000_001
            xi, yi = points[last_connected]

            for j in unconnected:
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                distances[j] = min(distances[j], distance)
                if distances[j] < min_distance:
                    min_distance = distances[j]
                    last_connected = j

            unconnected.remove(last_connected)
            result += min_distance

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().minCostConnectPoints_kruskal,
        Solution().minCostConnectPoints_prim,
        Solution().minCostConnectPoints_prim_cached,
    ]

    # fmt: off
    data = [
        ( [ [0, 0], [2, 2], [3, 10], [5, 2], [7, 0], ], 20, ), 
        ( [ [3, 12], [-2, 5], [-4, 1], ], 18, ), 
        ( [ [-1000000, -1000000], [1000000, 1000000] ], 4_000_000),
    ]
    # fmt: on

    for points, expected in data:
        for func in funcs:
            assert func(points) == expected


if __name__ == "__main__":
    pass
