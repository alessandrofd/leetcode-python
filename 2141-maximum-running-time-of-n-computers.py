"""
You have n computers. You are given the integer n and a 0-indexed integer
array batteries where the ith battery can run a computer for batteries[i]
minutes. You are interested in running all n computers simultaneously using
the given batteries.

Initially, you can insert at most one battery into each computer. After that
and at any integer time moment, you can remove a battery from a computer and
insert another battery any number of times. The inserted battery can be a
totally new battery or a battery from another computer. You may assume that
the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers
simultaneously.

Constraints:
    1 <= n <= batteries.length <= 10^5
    1 <= batteries[i] <= 10^9
"""


from typing import List


class Solution:
    def maxRunTime_sort_greedy(self, n: int, batteries: List[int]) -> int:
        """
        Suponha que tenhamos 3 computadores cada qual com baterias em ordem crescente
        de carga, de 0 a 2. Estas baterias devem ser aquelas com as maiores cargas.
        Além disso, temos uma bateria sobressalente com carga suficiente para manter
        os computadores funcionando pelo mesmo período de tempo. Para tanto, a bateria
        sobressalente terá que ter carga igual a
        (batteries[1] - batteries[0]) + 2 * (batteries[2] - batteries[1]).
        No entanto, para que os computadores 0 e 1 atinjam o tempo de funcionamento
        do computador 2, não podemos simplesmente contar com a carga restante
        da bateria sobressalente, pois todos os computadores têm que funcionar
        simultâneamente. Logo, temos que administrar não só a utilização da bateria
        sobressalente, mas de todas as baterias em uso.

        No primeiro caso, de estender o tempo de funcionamento do computador 0 para
        o mesmo tempo do computador 1, a solução envolve apenas a bateria
        sobressalente, pois trata-se de suplementar a bateria de apenas um computador.
        No entanto, no próximo passo, em que os computadores 0 e 1 dependem de
        uma complementação simultaneamente, temos que também manejar as baterias
        alimentando os computadores 0 e 1 antes mesmo que se esgotem. No momento em
        que os computadores 0 e 1 funcionaram até o limite da bateria original
        do computador 1 teremos gasto (batteries[1] - batteries[0]) da bateria
        sobressalente, que ainda terá uma carga de 2 * (batteries[2] - batteries[1]).
        Uma possível solução é que, na primeira estapa, ao invés de utilizar a bateria
        sobressalente apenas após a bateria do computador 0 se exaurir, nós a trocarmos
        quando a bateria do computador 0 ainda tiver uma carga de
        (batteries[2] - batteries[1]).

        É possível que a bateria do computador 0 tenham uma carga menor que
        (batteries[2] - batteries[1]). Não, pois como premissa alocamos inicialmente
        as baterias com maior carga ao computadores. Logo a bateria do computador 0
        terá necessariamente carga maior ou igual à da bateria sobressalente, que por
        sua vez tem carga igual a:
        (batteries[1] - batteries[0]) + 2 * (batteries[2] - batteries[1]).

        Este manejo de baterias é extensível a qualquer número de baterias?
        Considerando a bateria sobressalente tenha carga suficiente para suportar
        todos os n computadores até a capacidade da maior bateria. Basta trocarmos
        a bateria 0 pela bateria sobressalente quando sua carga restantes ainda for
        batteries[n] - batteries[1], a bateria 0 substituirá a bateria 1 quando esta
        atingir a carga de batteries[n] - batteries[2] e assim por diante.

        Caso tenhamos mais de uma bateria sobressalente, podemos somar suas cargas e
        tratá-las como uma única bateria e utilizar o mesmo processo descrito acima.

        Se a(s) bateria(s) sobressalent(s) tiver(em) carga suficiente para manter os
        computadores funcionando para além da capacidade da maior bateria, basta
        acrescentarmos, no processo acima, este adicional ao valor de batteries[n]
        """
        if n == len(batteries):
            return min(batteries)

        batteries.sort()
        live = batteries[-n:]
        total_charge = sum(batteries[:-n])

        for i in range(n - 1):
            charge = total_charge // (i + 1)
            if charge < live[i + 1] - live[i]:
                return live[i] + charge
            total_charge -= (live[i + 1] - live[i]) * (i + 1)

        return live[-1] + total_charge // n

    def maxRunTime_bin_search(self, n: int, batteries: List[int]) -> int:
        """
        A solução abaixo utiliza os mesmos conceitos da bateria sobressalente
        aplicados na solução anterior. O detalhe relevante aqui é que ao calcular
        a carga total (totalCharge) das baterias nós temos que descartar as cargas
        das baterias que excedam o valor que arbitramos como possível resposta
        (runningTime). runningTime não está restrito a qualquer carga individual já
        que o número de baterias pode exceder o número de computadores.
        """
        if n == len(batteries):
            return min(batteries)

        lo = 1
        hi = (sum(batteries) // n) + 1
        while lo < hi:
            running_time = (lo + hi) // 2
            charge = sum(min(running_time, c) for c in batteries) // n
            if running_time <= charge:
                lo = running_time + 1
            else:
                hi = running_time

        return lo - 1


def test_solution():
    """test"""

    funcs = [
        Solution().maxRunTime_sort_greedy,
        Solution().maxRunTime_bin_search,
    ]

    # fmt: off
    data = [
        (2, [3, 3, 3], 4),
        (2, [1, 1, 1, 1], 2),
        (3, [10, 10, 3, 5], 8),

    ]
    # fmt: on
    for n, batteries, expected in data:
        for func in funcs:
            assert func(n, batteries) == expected
