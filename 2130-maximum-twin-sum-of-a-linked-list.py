"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the
linked list is known as the twin of the (n-1-i)th node,
if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is
    the twin of node 2. These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin
sum of the linked list.

Constraints:
    The number of nodes in the list is an even integer in the range [2, 10^5].
    1 <= Node.val <= 10^5
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Dois ponteiros, um rápido e outro lento, para separar as metades da lista.
# Invertemos a primeira metade da lista ao mesmo tempo que a percorremos com os 
# dois ponteiros e somamos os nós ao percorrer simultaneamente as duas metades

class Solution:
    def pairSum_2pointers(self, head: ListNode) -> int:
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        first = prev
        second = slow
        max_twin = 0
        while second:
            max_twin = max(max_twin, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_twin

    def pairSum_list(self, head: ListNode) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        n = len(l)
        max_twin = 0
        for i in range(n // 2):
            max_twin = max(max_twin, l[i] + l[n - 1 - i])

        return max_twin


            


