"""
You are given two non-empty linked lists representing two non-negative
integers. The most significant digit comes first and each of their nodes
contains a single digit. Add the two numbers and return the sum as
a linked list.

You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have
    leading zeros.

Follow up: Could you solve it without reversing the input lists?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def to_stack(l):
            stack = []
            while l:
                stack.append(l.val)
                l = l.next
            return stack

        stack1 = to_stack(l1)
        stack2 = to_stack(l2)

        root = None
        carry = 0
        while stack1 or stack2 or carry:
            sum_stacks = carry

            if stack1:
                sum_stacks += stack1.pop()

            if stack2:
                sum_stacks += stack2.pop()

            carry = 1 if sum_stacks > 9 else 0
            root = ListNode(sum_stacks % 10, root)

        return root
