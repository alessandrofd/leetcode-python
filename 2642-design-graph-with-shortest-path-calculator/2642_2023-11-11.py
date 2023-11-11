from collections import defaultdict
from heapq import heappush, heappop
from math import inf
from itertools import product


class Graph_Dijkstra:
    def __init__(self, n, edges):
        self.n = n
        self.adjs = defaultdict(list)
        for from_node, to_node, cost in edges:
            self.adjs[from_node].append((cost, to_node))

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        self.adjs[from_node].append((cost, to_node))

    def shortestPath(self, node1, node2):
        n = self.n

        heap = [(0, node1)]

        cost_for_node = [inf] * n
        cost_for_node[node1] = 0

        while heap:
            curr_cost, curr_node = heappop(heap)

            if curr_node == node2:
                return curr_cost

            for adj_cost, adj_node in self.adjs[curr_node]:
                new_cost = curr_cost + adj_cost

                if new_cost >= cost_for_node[adj_node]:
                    continue

                cost_for_node[adj_node] = new_cost
                heappush(heap, (new_cost, adj_node))

        return -1


class Graph:
    def __init__(self, n, edges):
        adjs = [[inf] * n for _ in range(n)]
        for i in range(n):
            adjs[i][i] = 0

        for from_node, to_node, cost in edges:
            adjs[from_node][to_node] = cost

        for mid, start, end in product(range(n), repeat=3):
            adjs[start][end] = min(adjs[start][end], adjs[start][mid] + adjs[mid][end])

        self.n = n
        self.adjs = adjs

    def addEdge(self, edge):
        n = self.n
        adjs = self.adjs

        from_node, to_node, cost = edge
        for start, end in product(range(n), repeat=2):
            adjs[start][end] = min(
                adjs[start][end], adjs[start][from_node] + cost + adjs[to_node][end]
            )

    def shortestPath(self, node1, node2):
        cost = self.adjs[node1][node2]
        return -1 if cost == inf else cost
