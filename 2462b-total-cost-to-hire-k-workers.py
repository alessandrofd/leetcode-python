"""
You are given a 0-indexed integer array costs where costs[i] is the cost of
hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k
workers according to the following rules:

    You will run k sessions and hire exactly one worker in each session.

    In each hiring session, choose the worker with the lowest cost from either
    the first candidates workers or the last candidates workers. Break the tie
    by the smallest index.

        For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the
        first hiring session, we will choose the 4th worker (1) because they have
        the lowest cost [3,2,7,7,1,2].

        In the second hiring session, we will choose 1st worker because they
        have the same lowest cost as 4th worker but they have the smallest
        index [3,2,7,7,2]. Please note that the indexing may be changed in the
        process.

    If there are fewer than candidates workers remaining, choose the worker
    with the lowest cost among them. Break the tie by the smallest index.

    A worker can only be chosen once.

Return the total cost to hire exactly k workers.

Constraints:
    1 <= costs.length <= 10^5
    1 <= costs[i] <= 10^5
    1 <= k, candidates <= costs.length
"""

from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def totalCost_two_queues(self, costs: List[int], k: int, candidates: int) -> int:
        return 0

    def totalCost_one_queue(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        heap = []

        left = candidates
        for cost in costs[:candidates]:
            heappush(heap, (cost, 0))

        right = max(candidates, n - candidates) - 1
        for cost in costs[right + 1 :]:
            heappush(heap, (cost, 1))

        total_cost = 0
        while k:
            cost, side = heappop(heap)
            total_cost += cost
            k -= 1
            if left <= right:
                if side == 0:
                    heappush(heap, (costs[left], 0))
                    left += 1
                else:
                    heappush(heap, (costs[right], 1))
                    right -= 1

        return total_cost


def test_solution():
    """test"""

    funcs = [
        Solution().totalCost_one_queue,
        # Solution().totalCost_two_queues,
    ]

    # fmt: off
    data = [
        ([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11),
        ([1, 2, 4, 1], 3, 3, 4),
        ([25, 20, 60, 21, 11, 99, 55, 22, 83, 62, 12, 63, 100, 41, 33, 92, 13,
          92, 58, 85, 61, 93, 5, 46, 26, 25, 36, 27, 12, 30, 13, 52, 30, ],
          8, 22, 107),
    ]
    # fmt: on
    for costs, k, candidates, expected in data:
        for func in funcs:
            assert func(costs, k, candidates) == expected
