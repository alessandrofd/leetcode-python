"""
Given the root of a binary tree, return the maximum width of the given tree.]

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes
(the leftmost and rightmost non-null nodes), where the null nodes between
the end-nodes that would be present in a complete binary tree extending down
to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Constraints:
    The number of nodes in the tree is in the range [1, 3000].
    -100 <= Node.val <= 100
"""


# Utilizar BFS
# A cada nível atribuímos valores aos nós filhos baseados no valor do nó pai.
# Logo, o filho da esquerda será 2*n e o da direita 2*n + 1, onde n é o valor
# do nó pai. A largura máxima do nível será a diferença entre o último e o
# primeiro nó, da esquerda para a direita.
#
# Se a árvore for muito alta e, consequentemente, sua base muito larga,
# o contador estoura. No entanto, há um limite razoável no número de nós (3000).
# O próprio enunciado dá dicas sobre isso ao garantir que a resposta estará na
# faixa de um inteiro de 32-bits, considerando o sinal do inteiro a largura
# máxima seria 2 ** 16 - 1. Logo, em qualquer árvore com mais de 16 níveis
# temos que otimizar a forma de valorarmos os nós. A cada nível podemos
# considerar o nó mais à esquerda como referência e descontar o seu valor ao
# calcular os valores dos nós filhos do nível.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        width = 0
        queue = [(root, 0)]
        while queue:
            width = max(width, queue[-1][1] - queue[0][1] + 1)
            leftmost = queue[0][1]

            new_queue = []
            while queue:
                node, val = queue.pop(0)
                if node.left:
                    new_queue.append((node.left, 2 * (val - leftmost)))
                if node.right:
                    new_queue.append((node.right, 2 * (val - leftmost) + 1))

            queue = new_queue

        return width
