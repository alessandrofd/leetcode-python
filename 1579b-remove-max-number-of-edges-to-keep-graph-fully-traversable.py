"""
Alice and Bob have an undirected graph of n nodes and three types of edges:

    Type 1: Can be traversed by Alice only.
    Type 2: Can be traversed by Bob only.
    Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [typei, ui, vi] represents a
bidirectional edge of type typei between nodes ui and vi, find the maximum
number of edges you can remove so that after removing the edges, the graph
can still be fully traversed by both Alice and Bob. The graph is fully
traversed by Alice and Bob if starting from any node, they can reach all
other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and
Bob cannot fully traverse the graph.

Constraints:
    1 <= n <= 10^5
    1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)
    edges[i].length == 3
    1 <= typei <= 3
    1 <= ui < vi <= n
    All tuples (typei, ui, vi) are distinct.
"""

# Para resolver o problema ao invés de partir do grafo completo, o construímos
# do zero e a cada aresta acrescentada utilizamos DSU para verificar se ao
# final todos os nós estarão concectados. São dois os detalhes que divergem na
# aplicação normal do DSU. Criamos dois objetos distintos para cada um dos
# agentes, Alice e Bob, que deverão percorrer o grafo ao final. Estes objetos
# contêm as estruturas de dados e métodos necessários para implementar o DSU.
# Como procuramos o número mínimo de arestas necessárias para conectar todos
# o grafo, inicialmente acrescentamos a ele as arestas do tipo 3, que servem
# tanto a Alice quanto a Bob. Aplicamos estas arestas a ambos os objetos e
# em seguida aplicamos as arestas específicas a cada agente ao seus objeto
# respectivo. O segundo detalhe é que o método union(i, j) retorna se a aresta
# foi efetiva na junção de componentes desconcectados ou não. Ou seja, podemos
# tranquilamente adicionar todas as arestas ao grafo, sem qualquer
# discriminação (a não ser a ordem de acordo com seus tipos, conforme
# mencionado acima), que seremos capazes de contabilizar o número mínimo de
# arestas para conectar todos o grafo.


class Solution:
    def maxNumEdgesToRemove(self, num_nodes, edges):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().maxNumEdgesToRemove,
    ]

    data = [
        (4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]], 2),
        (4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]], 0),
        (4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]], -1),
    ]

    for num_nodes, edges, expected in data:
        for func in funcs:
            assert func(num_nodes, edges) == expected
