"""
You want to build some obstacle courses. You are given a 0-indexed integer
array obstacles of length n, where obstacles[i] describes the height of
the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of
the longest obstacle course in obstacles such that:

    You choose any number of obstacles between 0 and i inclusive.

    You must include the ith obstacle in the course.

    You must put the chosen obstacles in the same order as they appear in
    obstacles.

    Every obstacle (except the first) is taller than or the same height as
    the obstacle immediately before it.

Return an array ans of length n, where ans[i] is the length of the longest
obstacle course for index i as described above.

Constraints:
    n == obstacles.length
    1 <= n <= 10^5
    1 <= obstacles[i] <= 10^7
"""

# A cada obstáculo, decobrir o último obstáculo de tamanho igual ou menor e
# somar um. Parece uma aplicação de programação dinâmica, mas não trabalha com
# o elemento imediatamente anterior. O problema não pede os obstáculos
# selecionados, apenas o comprimento. Logo, podemos adorar uma abordagem greedy.
# Manteremos o registro dos circuitos pelos seus comprimentos. A cada
# comprimento registraremos a altura do menor obstáculo final dos circuitos com
# este comprimento. Selecionamos a menor altura pois ela abre maiores
# possibilidades de circuitos ainda mais longos com os obstáculos subsequentes.
# Para selecionarmos o ponto de inserção no vetor de comprimentos, utilizaremos
# uma busca binária.

from typing import List
from bisect import bisect_right


class Solution:
    """solution class"""

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """solution method"""

        heights = []
        result = []

        for obstacle_height in obstacles:
            if not heights or obstacle_height >= heights[-1]:
                heights.append(obstacle_height)
                result.append(len(heights))
            else:
                circuit_length = bisect_right(heights, obstacle_height)
                heights[circuit_length] = obstacle_height
                result.append(circuit_length + 1)

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().longestObstacleCourseAtEachPosition,
    ]

    data = [
        ([1, 2, 3, 2], [1, 2, 3, 3]),
        ([2, 2, 1], [1, 2, 1]),
        ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]),
    ]

    for obstacles, expected in data:
        for func in funcs:
            assert func(obstacles) == expected
