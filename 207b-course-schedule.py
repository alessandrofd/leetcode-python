"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first if
you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to
    first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import defaultdict, deque

# Algoritmo de Kahn


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        return False


def test_solution():
    """test"""

    funcs = [
        Solution().canFinish,
    ]

    # fmt: off
    data = [
        (2, [[1, 0]], True), 
        (2, [ [1, 0], [0, 1], ], False), 
    ]
    # fmt: on
    for num_courses, prerequisites, expected in data:
        for func in funcs:
            assert func(num_courses, prerequisites) == expected
