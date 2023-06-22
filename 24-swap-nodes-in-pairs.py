"""
Given a linked list, swap every two adjacent nodes and return its head. You
must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second


    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return head
        
    #     ghost = ListNode(-1, head)
    #     prev = ghost 
    #     first = head
    #     while first and first.next:
    #         second = first.next
    #         first.next = second.next
    #         second.next = first

    #         prev.next = second
    #         prev = first
    #         first = first.next

    #     return ghost.next