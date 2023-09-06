"""
Given the head of a singly linked list and an integer k, split the linked
list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should
have a size differing by more than one. This may lead to some parts being
null.

The parts should be in the order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal to parts
occurring later.

Return an array of the k parts.

Constraints:
    The number of nodes in the list is in the range [0, 1000].
    0 <= Node.val <= 1000
    1 <= k <= 50
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
    def splitListToParts(self, head, k):
        lists = [None] * k

        count_nodes = 0
        node = head
        while node:
            count_nodes += 1
            node = node.next

        base = count_nodes // k
        extra = count_nodes % k
        if base == 0:
            k = extra

        for i in range(k):
            lists[i] = head

            part_size = base + (1 if i < extra else 0)
            for _ in range(part_size - 1):
                head = head.next

            temp = head
            head = head.next
            temp.next = None

        return lists


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().splitListToParts,
    ]

    data = [
        [ [1, 2, 3],
            5,
            [ [1], [2], [3], [], [] ]
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            3,
            [ [1, 2, 3, 4], [5, 6, 7], [8, 9, 10], ]
        ],
    ]
    # fmt: on

    for nodes, k, expected in data:
        for func in funcs:
            parts = func(array_to_linked_list(nodes), k)
            output = []
            for part in parts:
                output.append(linked_list_to_array(part))
            assert output == expected


if __name__ == "__main__":
    # nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # ll = array_to_linked_list(nodes)
    # print(linked_list_to_array(ll))
    pass
