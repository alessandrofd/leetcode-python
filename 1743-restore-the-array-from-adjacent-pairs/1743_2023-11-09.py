from collections import defaultdict


class Solution:
    def restoreArray(self, adj_pairs):
        graph = defaultdict(list)
        for u, v in adj_pairs:
            graph[u].append(v)
            graph[v].append(u)

        curr = None
        for num, adjs in graph.items():
            if len(adjs) == 1:
                curr = num
                break

        prev = None
        nums = [curr]

        while len(nums) < len(graph):
            for adj in graph[curr]:
                if adj != prev:
                    prev = curr
                    curr = adj
                    nums.append(curr)
                    break

        return nums


def test_solution():
    """test"""

    funcs = [
        Solution().restoreArray,
    ]

    # fmt: off
    data = [
        [[[2,1],[3,4],[3,2]], [1,2,3,4]],
        [[[4,-2],[1,4],[-3,1]], [-2,4,1,-3]],
        [[[100000,-100000]], [100000,-100000]],
    ]
    # fmt: on

    for func in funcs:
        for adj_pairs, expected in data:
            output = func(adj_pairs)
            assert output == expected or output[::-1] == expected
