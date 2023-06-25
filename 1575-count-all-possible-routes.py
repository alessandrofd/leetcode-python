"""
You are given an array of distinct positive integers locations where
locations[i] represents the position of city i. You are also given integers
start, finish and fuel representing the starting city, ending city, and the
initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i
and 0 <= j < locations.length and move to city j. Moving from city i to
city j reduces the amount of fuel you have by |locations[i] - locations[j]|.
Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you
are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish.
Since the answer may be too large, return it modulo 109 + 7.

Constraints:
    2 <= locations.length <= 100
    1 <= locations[i] <= 10^9
    All integers in locations are distinct.
    0 <= start, finish < locations.length
    1 <= fuel <= 200
"""

from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    # Não deu TLE, apesar da versão em JS ter dado
    def countRoutes_dp_top_down(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        n = len(locations)
        memo = {}

        def travel(current_city: int, fuel_left: int) -> int:
            if fuel_left < 0:
                return 0
            if (current_city, fuel_left) in memo:
                return memo[(current_city, fuel_left)]

            routes = 1 if current_city == finish else 0
            for next_city in range(n):
                if next_city == current_city:
                    continue

                fuel_cost = abs(locations[next_city] - locations[current_city])

                routes = (
                    routes + travel(next_city, fuel_left - fuel_cost)
                ) % 1_000_000_007

            memo[((current_city, fuel_left))] = routes
            return routes

        return travel(start, fuel)

    def countRoutes_dp_bottom_up(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        n = len(locations)
        memo = [[0] * (fuel + 1) for _ in range(n)]
        memo[finish] = [1] * (fuel + 1)

        for fuel_left in range(0, fuel + 1):
            for current_city in range(n):
                for next_city in range(n):
                    if next_city == current_city:
                        continue

                    fuel_cost = abs(locations[next_city] - locations[current_city])
                    if fuel_cost > fuel_left:
                        continue

                    memo[current_city][fuel_left] = (
                        memo[current_city][fuel_left]
                        + memo[next_city][fuel_left - fuel_cost]
                    )

        return memo[start][fuel] % 1_000_000_007

    def countRoutes_dp_top_down_optimized(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        n = len(locations)
        fuel_costs = defaultdict(list)
        for city in range(n):
            for next_city in range(city + 1, n):
                fuel_cost = abs(locations[next_city] - locations[city])
                if fuel_cost > fuel:
                    continue
                fuel_costs[city].append((fuel_cost, next_city))
                fuel_costs[next_city].append((fuel_cost, city))
        for fuel_costs_city in fuel_costs.values():
            fuel_costs_city.sort()

        @cache
        def travel(current_city: int, fuel_left: int) -> int:
            routes = 1 if current_city == finish else 0

            for fuel_cost, next_city in fuel_costs[current_city]:
                # Como o combustível necessário para as próximas cidades estão
                # ordenados, não precisamos percorrer todas as possibilidades
                if fuel_cost > fuel_left:
                    break

                routes += travel(next_city, fuel_left - fuel_cost)

            return routes

        return travel(start, fuel) % 1_000_000_007


def test_solution():
    """test"""

    funcs = [
        Solution().countRoutes_dp_top_down,
        Solution().countRoutes_dp_bottom_up,
        Solution().countRoutes_dp_top_down_optimized,
    ]

    # fmt: off
    data = [
        ([2, 3, 6, 8, 4], 1, 3, 5, 4),
        ([4, 3, 1], 1, 0, 6, 5),
        ([5, 2, 1], 0, 2, 3, 0),
        ([2, 1, 5],  0,  0,  3,  2),
    ]
    # fmt: on
    for locations, start, finish, fuel, expected in data:
        for func in funcs:
            assert func(locations, start, finish, fuel) == expected
