"""
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not
passed as a parameter.

Do not modify the linked list.

Constraints:

    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"val = {self.val}, has next? = {self.next != None}"


def build_linked_list(arr, pos):
    if not arr:
        return None

    head = ListNode(arr.pop(0))
    indexed_nodes = [head]

    prev = head
    while arr:
        node = ListNode(arr.pop(0))
        indexed_nodes.append(node)
        prev.next = node
        prev = node

    if pos >= 0:
        prev.next = indexed_nodes[pos]

    return head




class Solution:
    def detectCycle_set(self, node: Optional[ListNode]) -> Optional[ListNode]:
        

    # Para resolver o problema temos que utilizar dois ponteiros percorrenco
    # a lista a velocidades diferentes. Considerando as seguintes definições:

    #   tartaruga = ponteiro lento, que avança uma posição a cada iteração
    #   lebre = ponteiro rápido, que avança duas posições por vez
    #   F = porção da lista Fora do ciclo
    #   C = porção da lista dentro do ciclo

    # O problema pede para encontrarmos o F, ou seja, a entrada do ciclo.

    # Se os ponteiros percorerrem a lista em suas respectivas velocidades e se a
    # lista tiver um ciclo, os ponteiros eventualmente se encontrarão. Vamos chamar
    # a distância entre o início do ciclo (F) e este ponto de encontro de intersec-
    # ção de "a". Ao se encontrarem os ponteiros terão percorrido as seguintes dis-
    # tâncias:

    #   tartaruga = F + a
    #   lebre = F + nC + a, onde n é um inteiro

    # como a lebre é duas vezes mais rápida que a tartaruga,

    #   2(F + a) = F + nC + a => F + a = nC => F = (C - a) + (n - 1)C

    # Se soltarmos nova tartaruga (ponteiro percorrendo uma única posição por
    # iteração) no início da lista , no tempo necessário para que percorra todo o
    # trecho da lista fora do ciclo (F), a tartaruga orignal percorrerá o que resta
    # para completar o ciclo a partir do ponto de intersecção (C - a) e um número
    # indeterminado de ciclos ((n - 1) * C) e parará justamente na entrada do ciclo.

    # Logo, a solução do problema será das pelo ponto onde as duas tartarugas se
    # encontrarem

    def detectCycle_two_pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


def test_detectCycle():
    """test minEatingSpeed"""

    funcs = [Solution().detectCycle_set, Solution().detectCycle_two_pointers]

    data = [
        ([3, 2, 0, -4], 1, 2),
        ([1, 2], 0, 1),
        ([1], -1, None),
        ([], -1, None),
        ([-1, -7, 7, -4, 19, 6, -9, -5, -2, -5], 6, -9),
        ([1, 2], -1, None),
    ]

    for arr, pos, output in data:
        head = build_linked_list(arr, pos)
        for func in funcs:
            if not output:
                assert func(head) is None
            else:
                assert func(head).val == output
