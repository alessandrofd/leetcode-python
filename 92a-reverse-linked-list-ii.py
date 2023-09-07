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


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(arr):
    """Array to LinkedList"""
    head = None
    for i in range(len(arr) - 1, -1, -1):
        head = ListNode(arr[i], head)

    return head


def linked_list_to_array(head):
    """LinkedList to Array"""
    arr = []
    node = head
    while node:
        arr.append(node.val)
        node = node.next

    return arr


class Solution:
    def reverseBetween(self, head, left, right):
        pass


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
