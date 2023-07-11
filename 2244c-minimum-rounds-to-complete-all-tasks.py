"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the
difficulty level of a task. In each round, you can complete either 2 or 3
tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is
not possible to complete all the tasks.

Constraints:
    1 <= tasks.length <= 10^5
    1 <= tasks[i] <= 10^9
"""
from typing import List
from collections import Counter
from math import ceil


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freqs = Counter(tasks)

        rounds = 0
        for freq in freqs.values():
            if freq == 1:
                return -1

            rounds += ceil(freq / 3)

        return rounds


def test_solution():
    """test"""

    funcs = [
        Solution().minimumRounds,
    ]

    # fmt: off
    data = [
        ([2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4),
        ([2, 3, 3], -1),
        ([5, 5, 5, 5], 2),
    ]
    # fmt: on
    for tasks, expected in data:
        for func in funcs:
            assert func(tasks) == expected
