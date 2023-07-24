"""
Given an integer n, return a list of all possible full binary trees with
n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may
return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or
2 children.

Constraints:
    1 <= n <= 20
"""

# Programação dinâmica tendo como dimensão relevante o número de nós.
# Os nós de uma árvore binárias completas tem obrigatoriamente 0 ou 2 filhos,
# logo a árvore só pode ter número ímpar de nós. Podemos decompor o problema ao
# dividir os nós restantes (subtraído o nó raiz), n - 1, entre os lados
# esquerdos e direito. Devemos considerar ainda que cada ramo da árvore também
# deve ser uma árvore binária completa, logo as duas parcelas, esquerda e
# direita, também devem ser ímpares. Enquanto o lado esquerdo variar entre 1 e
# n - 2 nós, com incrementos de 2 unidades para manter o número ímpar de nós,
# o lado direito variará de n - 2 a 1. As árvores resultantes serão compostas
# pela raiz e todas as (n/2)^2 combinações de ramos esquerdos e direitos.


from typing import List, Optional
from itertools import product
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT_bottom_up_dp(self, n: int) -> List[Optional[TreeNode]]:
        """
        Bottom-Up Dynamic Programming
        """
        return []

    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        Top-Down Dynamic Programming
        """
        return []
