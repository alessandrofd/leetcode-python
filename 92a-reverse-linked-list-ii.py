"""
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
"""

from __future__ import annotations


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def array_to_linked_list(arr: list[int]) -> ListNode | None:
    """Array to LinkedList"""
    head = None
    for i in range(len(arr) - 1, -1, -1):
        head = ListNode(arr[i], head)

    return head


def linked_list_to_array(head: ListNode) -> list[int]:
    """LinkedList to Array"""
    arr = []
    node = head
    while node:
        arr.append(node.val)
        node = node.next

    return arr


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        before = ListNode(-1, head)
        previous_node = before
        for i in range(1, left):
            previous_node = previous_node.next

        first_node = previous_node.next
        for i in range(left, right):
            next_node = first_node.next
            first_node.next = next_node.next
            next_node.next = previous_node.next
            previous_node.next = next_node

        return before.next


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().reverseBetween,
    ]

    data = [
        [[1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]],
        [[5], 1, 1, [5]],
    ]
    # fmt: on

    for nodes, left, right, expected in data:
        for func in funcs:
            head = array_to_linked_list(nodes)
            output = linked_list_to_array(func(head, left, right))
            assert output == expected


if __name__ == "__main__":
    # nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # ll = array_to_linked_list(nodes)
    # print(linked_list_to_array(ll))
    pass
