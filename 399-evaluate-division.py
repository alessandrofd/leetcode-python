"""
You are given an array of variable pairs equations and an array of real
numbers values, where equations[i] = [Ai, Bi] and values[i] represent
the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents
a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents
the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.

Constraints:
    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation_pre_calculation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), q in zip(equations, values):
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = q
            graph[v][u] = 1 / q

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]

        return [graph[u].get(v, -1) for u, v in queries]

    def calcEquation_backtrack(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), q in zip(equations, values):
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = q
            graph[v][u] = 1 / q

        def backtrack(u, v, q, visited):
            if v in graph[u]:
                return q * graph[u][v]

            visited.add(u)

            for w in graph[u]:
                if w in visited:
                    continue
                result = backtrack(w, v, q * graph[u][w], visited)
                if result != -1:
                    return result

            visited.remove(u)
            return -1

        result = []
        for u, v in queries:
            if not (u in graph and v in graph):
                result.append(-1)
            else:
                result.append(backtrack(u, v, 1, set()))
        return result


def test_solution():
    """test"""

    funcs = [
        Solution().calcEquation_pre_calculation,
        Solution().calcEquation_backtrack,
    ]

    data = [
        (
            [
                ["a", "b"],
                ["b", "c"],
            ],
            [2.0, 3.0],
            [
                ["a", "c"],
                ["b", "a"],
                ["a", "e"],
                ["a", "a"],
                ["x", "x"],
            ],
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        ),
        (
            [
                ["a", "b"],
                ["b", "c"],
                ["bc", "cd"],
            ],
            [1.5, 2.5, 5.0],
            [
                ["a", "c"],
                ["c", "b"],
                ["bc", "cd"],
                ["cd", "bc"],
            ],
            [3.75000, 0.40000, 5.00000, 0.20000],
        ),
        (
            [["a", "b"]],
            [0.5],
            [
                ["a", "b"],
                ["b", "a"],
                ["a", "c"],
                ["x", "y"],
            ],
            [0.50000, 2.00000, -1.00000, -1.00000],
        ),
        (
            [
                ["a", "b"],
                ["c", "d"],
            ],
            [1.0, 1.0],
            [
                ["a", "c"],
                ["b", "d"],
                ["b", "a"],
                ["d", "c"],
            ],
            [-1.00000, -1.00000, 1.00000, 1.00000],
        ),
    ]

    for equations, values, queries, expected in data:
        for func in funcs:
            assert func(equations, values, queries) == expected
