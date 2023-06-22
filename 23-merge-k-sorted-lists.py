"""
You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional
from heapq import heapify, heappush, heappop


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Solution class"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Usando pririty queue"""

        if not lists or len(lists) == 0:
            return None

        queue = []
        for head in lists:
            while head:
                heappush(queue, (head.val, head))
                head = head.next

        dummy = ListNode()
        tail = dummy
        while queue:
            _, node = heappop(queue)
            tail.next = node
            tail = node
        tail.next = None

        return dummy.next
