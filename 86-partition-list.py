"""
 * Given the head of a linked list and a value x, partition it such that all
 * nodes less than x come before nodes greater than or equal to x.
 *
 * You should preserve the original relative order of the nodes in each of the
 * two partitions.
 *
 * Constraints:
 *    The number of nodes in the list is in the range [0, 200].
 *    -100 <= Node.val <= 100
 *    -200 <= x <= 200
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def build_list(nums):
        """
        Retorna uma lista encadeada a partir de um vetor (lista) de números
        """
        if len(nums) == 0:
            return None

        before = ListNode()
        node = before

        for num in nums:
            node.next = ListNode(num)
            node = node.next

        return before.next

    @staticmethod
    def destroy_list(head):
        """
        Retorna um vetor (lista) de números a partir de uma lista encadeada
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return nums


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head, greater_head = ListNode(), ListNode()
        less, greater = less_head, greater_head

        while head:
            if head.val < x:
                less.next = head
                less = head
            else:
                greater.next = head
                greater = head

            head = head.next

        less.next = greater_head.next
        greater.next = None
        return less_head.next


def test_solution():
    """test"""

    funcs = [
        Solution().partition,
    ]

    # fmt: off
    data = [
        ([1, 4, 3, 2, 5, 2], 3, [1,2,2,4,3,5]),
        ([2, 1], 2, [1,2]),
    ]
    # fmt: on
    for nums, x, expected in data:
        for func in funcs:
            linked_list = ListNode.build_list(nums)
            nums = ListNode.destroy_list(func(linked_list, x))
            assert nums == expected


if __name__ == "__main__":
    l = [1, 4, 3, 2, 5, 2]
    ll = ListNode.build_list(l)
    print(ListNode.destroy_list(ll))
