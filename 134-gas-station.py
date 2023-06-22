"""
There are n gas stations along a circular route, where the amount of gas at
the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to
travel from the ith station to its next (i + 1)th station. You begin the
journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's
index if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be
unique

Constraints:
        n == gas.length == cost.length
        1 <= n <= 10^5
        0 <= gas[i], cost[i] <= 10^4
"""


# Podemos decompor a solução do problema em duas condições distintas. Primeiro,
# do ponto de partida em diante, não podemos ficar "no negativo". Em seguida,
# deve haver gasolina suficiente para dar a volta completa no circuito,
# independentemente de onde começamos. Logo, percorreremos todos os pontos para
# determinar o primeiro ponto em que a condição inicial seja atendida. Se, ao
# final de contabilizarmos todos os pontos, a segunda condição também for
# atendida, teremos a solução do problema.

from typing import List


class Solution:
    """solution class"""

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """solution method"""
        num_gas_stations = len(gas)
        starting_station = 0
        gas_tank = 0
        final_gas_tank = 0

        for i in range(num_gas_stations):
            final_gas_tank += gas[i] - cost[i]
            gas_tank += gas[i] - cost[i]
            if gas_tank < 0:
                gas_tank = 0
                starting_station = i + 1

        return starting_station if final_gas_tank >= 0 else -1


def test_solution():
    """test"""

    funcs = [
        Solution().canCompleteCircuit,
    ]

    data = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([3, 1, 1], [1, 2, 2], 0),
    ]

    for gas, cost, expected in data:
        for func in funcs:
            assert func(gas, cost) == expected
