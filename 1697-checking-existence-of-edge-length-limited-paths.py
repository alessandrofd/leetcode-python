"""
An undirected graph of n nodes is defined by edgeList, where
edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with
distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to
determine for each queries[j] whether there is a path between pj and qj such
that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and
the jth value of answer is true if there is a path for queries[j] is true,
and false otherwise.

Constraints:
    2 <= n <= 10^5
    1 <= edgeList.length, queries.length <= 10^5
    edgeList[i].length == 3
    queries[j].length == 3
    0 <= ui, vi, pj, qj <= n - 1
    ui != vi
    pj != qj
    1 <= disi, limitj <= 10^9
    There may be multiple edges between two nodes.
"""

# A cada query eliminamos as arestas do grafo com peso superior ao limite da
# query. Desta forma podemos aplicar DSU para saber se ambas os nós da query
# continuam ligados. Para otimizar o algoritmo ordenamos as queries pelos seus
# limites em ordem ascendente e aplicamos paulatinamente o limite ao DSU. Desta
# forma não temos que calculá-lo do zero a cada query.

class Solution:
    def distanceLimitedPathsExist(self, num_nodes, edges, queries):
        num_edges = len(edges)
        num_queries = len(queries)
        result = [None] * num_queries
        parents = list(range(num_nodes))
        ranks = [1] * num_nodes

        sorted_edges = sorted(edges, key=lambda edge: edge[2])
        indexed_queries = [queries[i] + [i] for i in range(num_queries)]
        sorted_queries = sorted(indexed_queries, key=lambda query: query[2])

        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        
        def union(i, j):
            i = find(i)
            j = find(j)

            if i == j:
                return
            
            if ranks[i] > ranks[j]:
                parents[j] = i
                ranks[i] += ranks[j]
            else:
                parents[i] = j
                ranks[j] += ranks[i]


        edges_index = 0
        for orig, dest, limit, result_index in sorted_queries:
            while edges_index < num_edges and sorted_edges[edges_index][2] < limit:
                i, j, _ = sorted_edges[edges_index]
                union(i, j)
                edges_index += 1
            result[result_index] = find(orig) == find(dest)
    
        return result


def test_solution():
    """test"""

    funcs = [
        Solution().distanceLimitedPathsExist,
    ]

    data = [
        (3, [ [0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16] ], [ [0, 1, 2], [0, 2, 5] ], [False, True]), 
        (5, [ [0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13] ], [ [0, 4, 14], [1, 4, 13] ], [True, False])
    ]

    for num_nodes, edges, queries, expected in data:
        for func in funcs:
            assert func(num_nodes, edges, queries) == expected



