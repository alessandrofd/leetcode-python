"""
There is a group of n members, and a list of various crimes they could commit.
The ith crime generates a profit[i] and requires group[i] members to participate
in it. If a member participates in one crime, that member can't participate
in another crime.

Let's call a profitable scheme any subset of these crimes that generates at
least minProfit profit, and the total number of members participating in that
subset of crimes is at most n.Return the number of schemes that can be chosen.
Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
    1 <= n <= 100
    0 <= minProfit <= 100
    1 <= group.length <= 100
    1 <= group[i] <= 100
    profit.length == group.length
    0 <= profit[i] <= 100
"""

# Programaçaõ dinâmica, aparentemente toda questão difícil do LeetCode requer
# programação dinâmica. Duas dimensões são bastante claras: os golpes avaliados
# e a quantidade de criminosos necessária. No entanto, o problema estabelece um t
# erceiro critério, uma lucro mínimo - o que indica a necessidade de ainda mais
# uma dimensão, limitada ao lucro mínimo necessário.
#
# Uma escolha interessante é se a análise deve partir de todos os golpes
# aplicados ou de nenhum golpe aplicado. A escolha afetará o caso base e como
# caracterizaremos o resultado final. Caso optemos por iniciar do final, o que
# de fato optamos para a resolução deste problemas, o caso base será que, se
# atendido o critério de lucro mínimo, a quantidade de esquemas será 1,
# independente da quantidade de criminosos disponíveis, e o resultado final
# será fornecido quando atingirmos o ponto em que nenhum golpe foi aplicado
# ainda e todos os criminosos estão disponíveis.
#
# Por outro lado, podemos optar por iniciar a nossa análise com nenhum golpe
# aplicado e todos os criminosos disponíveis - situação que caracteriza o
# resultado final na outra opção. Nesta opção, o caso base não terá relação com
# o critério de lucro mínimo, já que o lucro será acrescido à medida que os
# golpes forem aplicados. Logo, o caso base assume outra significado de que a
# opção de não se aplicar qualquer golpe é uma opção válida. No entanto, esta
# opção também estabelece que o lucro inicial será zero. Logo, todas as
# combinações de criminosos disponíveis e lucro zero dever ser iniciada com 1.
# O resultado final, desta forma será dado quando aplicarmos todos os golpes
# (possíveis, dado os critérios de criminosos necessários) nas situações em que
# atingirmos o lucro mínimo pedido.
#
# A transição apresenta duas possibilidades, ou não aplicamos o golpe e
# simplesmente replicamos os valores do golpe anterior, mantendo fixos os
# valores de criminosos utilizados e de lucro obtido. Ou aplicamos o golpe,
# caso a quantidade de criminosos disponíveis seja suficiente.
# O número de esquemas é a soma destas duas possibilidades.
# Como estamos processando de trás para a frente temos que calcular todas as
# combinações de criminosos disponíveis e lucro obtido. Isto porque não sabemos
# quais as condições que as próximas iterações produzirão.
#
# Transicões:
#  sem golpe = dp[con][criminals][profit] = dp[con + 1][criminals][profit]
#  com golpe :
#    if (addedCriminals <= totalCriminals)
#      dp[con][criminals][profit] = dp[con + 1][addedCriminals][addedProfit]
#   onde:
#      addedCriminals = criminals + groups[con]
#      addProfit = Math.min(minProfit, profit + profits[con])


# Começando pela situação em que nenhum golpe foi aplicado. A otimização de
# espaço, eliminando a dimensão do golpe, permite que apliquemos otimização no
# processamento das quantidades de criminosos disponíveis. Limitamos a avalição
# a apenas os valores que atendam a quantidade mínima de criminosos exigida pelo
# golpe. As quantidade inferiores de criminosos são mantidos os valores da
# iteração anterior.


class Solution:
    def profitableSchemes(self, total_criminals, min_profit, groups, profits):
        MOD = 1e9 + 7
        total_cons = len(profits)
        dp = [[0 for _ in range(min_profit + 1)] for _ in range(total_criminals + 1)]

        for criminals in range(total_criminals + 1):
            dp[criminals][0] = 1

        for con in range(total_cons):
            for criminals in range(total_criminals, groups[con] - 1, -1):
                for profit in range(min_profit, -1, -1):
                    prev_criminals = criminals - groups[con]
                    prev_profit = max(0, profit - profits[con])
                    dp[criminals][profit] += dp[prev_criminals][prev_profit]
                    dp[criminals][profit] = int(dp[criminals][profit] % MOD)

        return dp[total_criminals][min_profit]


def test_solution():
    """test"""

    funcs = [
        Solution().profitableSchemes,
    ]

    data = [
        (5, 3, [2, 2], [2, 3], 2),
        (10, 5, [2, 3, 5], [6, 7, 8], 7),
    ]

    for total_criminals, min_profit, groups, profits, expected in data:
        for func in funcs:
            assert func(total_criminals, min_profit, groups, profits) == expected
