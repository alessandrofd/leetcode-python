"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

Constraints:
    2 <= asteroids.length <= 10^4
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""

# Os sinais não indicam apenas direçoes opostas positivo se movimentará para a
# direita e negativa para a esquerda. Logo, se tivermos uma sequência positivo
# seguido de um negativo, teremos uma colisão. No entanto, se tivermos negativo
# seguido de um positivo, os asteroids se afastarão e não colidirão.

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                previous = stack.pop()
                if previous > -asteroid:
                    asteroid = previous
                elif previous == -asteroid:
                    asteroid = 0

            if asteroid:
                stack.append(asteroid)

        return stack


def test_solution():
    """test"""

    funcs = [
        Solution().asteroidCollision,
    ]

    # fmt: off
    data = [
        ([5, 10, -5],[5,10], ),
        ([8, -8],[], ),
        ([10, 2, -5],[10], ),
        ([-2, -1, 1, 2],[-2,-1,1,2], ),
    ]
    # fmt: on
    for asteroids, expected in data:
        for func in funcs:
            assert func(asteroids) == expected
