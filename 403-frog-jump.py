"""
A frog is crossing a river. The river is divided into some number of units,
and at each unit, there may or may not exist a stone. The frog can jump on a
stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog can cross the river by landing on the last stone.
Initially, the frog is on the first stone and assumes the first jump must be
1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k,
or k + 1 units. The frog can only jump in the forward direction.

Constraints:
    2 <= stones.length <= 2000
    0 <= stones[i] <= 2^31 - 1
    stones[0] == 0
    stones is sorted in a strictly increasing order.
"""

from typing import List
from functools import cache
from bisect import bisect_left
from collections import defaultdict, deque


class Solution:
    def canCross_dp_top_down(self, stones: List[int]) -> bool:
        """
        DP Top-Down
        """
        n = len(stones)
        if stones[1] != 1:
            return False
        if n == 2:
            return True

        @cache
        def dfs(i, k):
            if i == n - 1:
                return True

            result = False

            for jump in range(max(1, k - 1), k + 2):
                target = stones[i] + jump
                next_stone = bisect_left(stones, target, lo=i + 1)
                if next_stone < n and stones[next_stone] == target:
                    result = result or dfs(next_stone, jump)

            return result

        return dfs(1, 1)

    def canCross_dp_bottom_up(self, stones: List[int]) -> bool:
        """
        DP Bottom-Up
        """
        n = len(stones)
        if stones[1] != 1:
            return False
        if n == 2:
            return True

        stones_map = {n: i for i, n in enumerate(stones)}

        dp = defaultdict(list)
        dp[1].append(1)
        max_jump = 1

        for i in range(2, n):
            for j in range(1, max_jump + 2):
                previous = stones[i] - j
                if previous in stones_map:
                    for k in range(max(1, j - 1), min(max_jump, j + 1) + 1):
                        if k in dp[stones_map[previous]]:
                            dp[i].append(j)
                            max_jump = max(max_jump, j)

        return len(dp[n - 1]) > 0

    def canCross_bfs(self, stones: List[int]) -> bool:
        """
        BFS
        """
        n = len(stones)
        if stones[1] != 1:
            return False
        if n == 2:
            return True

        stones_set = set(stones)
        visited = set()

        stack = [(1, 1)]
        while stack:
            stone, jump = stack.pop()
            for next_jump in range(max(1, jump - 1), jump + 2):
                next_stone = stone + next_jump

                if next_stone in stones_set and (next_stone, next_jump) not in visited:
                    if next_stone == stones[-1]:
                        return True

                    stack.append((next_stone, next_jump))

                visited.add((next_stone, next_jump))

        return False


def test_solution():
    """test"""

    funcs = [
        Solution().canCross_dp_top_down,
        Solution().canCross_dp_bottom_up,
        Solution().canCross_bfs,
    ]

    # fmt: off
    data = [
        [[0, 1, 3, 5, 6, 8, 12, 17], True],
        [[0, 1, 2, 3, 4, 8, 9, 11], False],
        [[0, 1, 2147483647], False],
        [[0, 1, 3, 6, 10, 13, 15, 18], True]
    ]
    # fmt: on

    for stones, expected in data:
        for func in funcs:
            assert func(stones) == expected


if __name__ == "__main__":
    pass
