"""
Given the head of a singly linked list where elements are sorted in ascending
order, convert it to a height-balanced binary search tree.

Constraints:
    The number of nodes in head is in the range [0, 2 * 10^4].
    -10^5 <= Node.val <= 10^5
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    # O primeiro passo é descobrir o "meio" da lista encadeada. Podemos fazer isso
    # lendo a lista e colocando os seus elementos em um vetor.

    # Em seguida construímos a árvore recursivamente ao selecionar o elemento
    # central do vetor como um nó raiz e os trechos do vetor que este elemento
    # separa serão os argumentos para a próxima iteração da recursão até que
    # cheguemos a um único elemento.

    def sortedListToBST_array(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Utilizando list como apoio"""

    # Na solução anterior precisamos criar um vetor de apoio para que pudéssemos
    # acessar randômicamente os elementos da lista encadeada. No entanto, se
    # respeitarmos a ordem dos valores na contrução da árvore binária, o vetor
    # é desnecessário.

    # Para tanto, partimos, da mesma forma que na solução anterior, do elemento
    # central da lista. Logo, em primeiro lugar, devemos percorrer toda a lista
    # para determinar o seu comprimento. Mas, neste caso, precisamos apenas do seu
    # índice e não do nó propriamente dito. Para tanto, é preciso primeiro contruir
    # integralmente o ramo da esquerda ao elemento central, então o nó que
    # representará o elemento central e, por fim, o ramo da direita. A cada nó da
    # árvore binária criada avançamos para o próximo nó da lista encadeada. A
    # sincronia entre a criação da esqueda para a direita da árvore e o avanço na
    # lista encadeada é o que torna o vetor de apoio desenecessário.

    def sortedListToBST_no_array(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Sem list de apoio"""
