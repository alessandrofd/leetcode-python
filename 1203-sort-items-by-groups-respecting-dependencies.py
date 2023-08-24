"""
There are n items each belonging to zero or one of m groups where group[i] is
the group that the i-th item belongs to and it's equal to -1 if the i-th item
belongs to no group. The items and the groups are zero indexed. A group can
have no item belonging to it.

Return a sorted list of the items such that:

    The items that belong to the same group are next to each other in the
    sorted list.

    There are some relations between these items where beforeItems[i] is a
    list containing all the items that should come before the i-th item in the
    sorted array (to the left of the i-th item).

Return any solution if there is more than one solution and return an empty
list if there is no solution.

Constraints:
    1 <= m <= n <= 3 * 10^4
    group.length == beforeItems.length == n
    -1 <= group[i] <= m - 1
    0 <= beforeItems[i].length <= n - 1
    0 <= beforeItems[i][j] <= n - 1
    i != beforeItems[i][j]
    beforeItems[i] does not contain duplicates elements.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], before_items: List[List[int]]
    ) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in before_items[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[curr] == group[prev]:
                    continue

                group_graph[group[prev]].append(group[curr])
                group_indegree[group[curr]] += 1

        def topological_sort(graph, indegree):
            n = len(indegree)
            visited = []
            stack = deque([node for node in range(n) if indegree[node] == 0])

            while stack:
                node = stack.popleft()
                visited.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        stack.append(neighbor)

            if len(visited) == n:
                return visited
            return []

        item_linear = topological_sort(item_graph, item_indegree)
        group_linear = topological_sort(group_graph, group_indegree)

        if not item_linear or not group_linear:
            return []

        group_items = defaultdict(list)
        for item in item_linear:
            group_items[group[item]].append(item)

        result = []
        for group_index in group_linear:
            result += group_items[group_index]

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().sortItems,
    ]

    # fmt: off
    data = [
        (
            8,
            2,
            [-1, -1, 1, 0, 0, 1, 0, -1],
            [[], [6], [5], [6], [3, 6], [], [], []],
            [6, 3, 4, 1, 5, 2, 0, 7],
        ),
        (
            8,
            2,
            [-1, -1, 1, 0, 0, 1, 0, -1],
            [[], [6], [5], [6], [3], [], [4], []],
            []
        ),
    ]
    # fmt: on

    for n, m, group, before_items, expected in data:
        for func in funcs:
            assert func(n, m, group, before_items) == expected


if __name__ == "__main__":
    print(
        Solution().sortItems(
            8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]
        )
    )
