"""
You have k bags. You are given a 0-indexed integer array weights where
weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

    No bag is empty.

    If the ith marble and jth marble are in a bag, then all marbles with
    an index between the ith and jth indices should also be in that same bag.

    If a bag consists of all the marbles with an index from i to j inclusively,
    then the cost of the bag is weights[i] + weights[j].

The score after distributing the marbles is the sum of the costs of all
the k bags.

Return the difference between the maximum and minimum scores among marble
distributions.

Constraints:
    1 <= k <= weights.length <= 10^5
    1 <= weights[i] <= 10^9
"""

from typing import List

# A solução é considerar não as bolinhas de gude, mas as fronteiras entre elas
# já que o custo de um saco é dado justamente pela diferença de peso
# da primeira e da última bolinha no saco.

# Como o problema pede a diferença entre o maior e o menor custo, a primeira e
# a última bolinha da sequência podem ser ignoradas.

# Ao ordenarmos as fronteiras, que em última análise representam como dividimos
# as bolinhas pelos sacos, a resposta será o somatório da diferença entre
# as k-1 maiores e menores fronteiras.

from itertools import pairwise


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k in (1, len(weights)):
            return 0

        boundaries = [x + y for x, y in pairwise(weights)]
        boundaries.sort()
        return sum(boundaries[-(k - 1) :]) - sum(boundaries[: (k - 1)])


def test_solution():
    """test"""

    funcs = [
        Solution().putMarbles,
    ]

    # fmt: off
    data = [
        ([1, 3, 5, 1], 2, 4),
        ([1, 3], 2, 0),
    ]
    # fmt: on

    for weights, k, expected in data:
        for func in funcs:
            assert func(weights, k) == expected
