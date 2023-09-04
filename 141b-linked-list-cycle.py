"""
Given head, the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if there is some node in the list that can
be reached again by continuously following the next pointer. Internally, pos
is used to denote the index of the node that tail's next pointer is connected
to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

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


def build_linked_list(nodes):
    if len(nodes) == 0:
        return None

    before = ListNode(-1)
    node = before

    while nodes:
        node.next = ListNode(nodes.pop(0))
        node = node.next

    return before.next


def close_cycle(head, pos):
    tail = None
    node = head
    count = 0
    insert = None
    while node:
        if count == pos:
            insert = node
        count += 1
        tail = node
        node = node.next

    tail.next = insert


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's cycle finding algorithm or Hare-Tortoise algorithm is a pointer
        algorithm that uses only two pointers, moving through the sequence at
        different speeds. This algorithm is used to find a loop in a linked list.
        It uses two pointers one moving twice as fast as the other one. The faster
        one is called the fast pointer and the other one is called the slow pointer.

        How Does Floyd's Cycle Finding Algorithm Works?

        While traversing the linked list one of these things will occur:

            The Fast pointer may reach the end (NULL) this shows that there is no
            loop in the linked list.

            The Fast pointer again catches the slow pointer at some time therefore a
            loop exists in the linked list.
        """

        return False


def test_solution():
    """test"""

    funcs = [
        Solution().hasCycle,
    ]

    data = [
        [[3, 2, 0, -4], 1, True],
        [[1, 2], 0, True],
        [[1], -1, False],
    ]

    for nodes, pos, expected in data:
        head = build_linked_list(nodes)
        if pos >= 0:
            close_cycle(head, pos)
        for func in funcs:
            assert func(head) == expected


if __name__ == "__main__":
    head = build_linked_list([3, 2, 0, -4])
    close_cycle(head, 1)
    node = head
    while node:
        print(node.val)
        if node.val == -4:
            break
        node = node.next
    print(node.next.val)
