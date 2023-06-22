"""
You are given an array of integers stones where stones[i] is the weight of
the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest
two stones and smash them together. Suppose the heaviest two stones have
weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y
    has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left,
return 0.

Constraints:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""

from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones):
        pq = [-1 * stone for stone in stones]
        heapify(pq)

        while len(pq) >= 2:
            stone1 = heappop(pq)
            stone2 = heappop(pq)
            if stone1 != stone2:
                heappush(pq, stone1 - stone2)

        result = 0
        if pq:
            result = -heappop(pq)
        return result


def test_solution():
    """test"""

    funcs = [
        Solution().lastStoneWeight,
    ]

    data = [([2, 7, 4, 1, 8, 1], 1), ([1], 1)]

    for stones, expected in data:
        for func in funcs:
            assert func(stones) == expected
