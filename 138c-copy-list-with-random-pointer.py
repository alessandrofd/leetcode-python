"""
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new
nodes should point to new nodes in the copied list such that the pointers in
the original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where
X.random --> Y, then for the corresponding two nodes x and y in the copied
list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each
node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val

    random_index: the index of the node (range from 0 to n-1) that the random
    pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Constraints:
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random is null or is pointing to some node in the linked list.
"""


class Node:
    """Definition for a Node."""

    def __init__(self, val, next_node=None, random=None):
        self.val = int(val)
        self.next = next_node
        self.random = random


def array_to_linked_list(arr):
    """Array to LinkedList"""
    n = len(arr)

    nodes = [None] * n
    head = None
    for i in range(n - 1, -1, -1):
        head = Node(arr[i][0], head)
        nodes[i] = head

    for i in range(n):
        random = arr[i][1]
        if random is not None:
            nodes[i].random = nodes[random]

    return head


def linked_list_to_array(head):
    """LinkedList to Array"""
    node_to_index = {}
    node = head
    i = 0
    while node:
        node_to_index[node] = i
        node = node.next
        i += 1

    arr = []
    node = head
    while node:
        random_index = None
        if node.random:
            random_index = node_to_index[node.random]
        arr.append([node.val, random_index])
        node = node.next

    return arr


class Solution:
    def copyRandomList(self, head):
        pass


# Por algum motivo pytest está dando erro ... não consegui descobrir
def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().copyRandomList,
    ]

    data = [
        [
            [ [7, None], [13, 0], [11, 4], [10, 2], [1, 0], ],
            [ [7, None], [13, 0], [11, 4], [10, 2], [1, 0], ],
        ],
        # [
        #     [ [1, 1], [2, 1], ],
        #     [ [1, 1], [2, 1], ],
        # ],
        # [
        #     [ [3, None], [3, 0], [3, None], ],
        #     [ [3, None], [3, 0], [3, None], ],
        # ],
    ]
    # fmt: on

    for nodes, expected in data:
        for func in funcs:
            head = array_to_linked_list(nodes)

            node = head
            while node:
                next_val = node.next.val if node.next else None
                random_val = node.random.val if node.random else None
                print(node.val, next_val, random_val)
                node = node.next

            output = linked_list_to_array(func(head))
            assert func(output) == expected


if __name__ == "__main__":
    nodes = [
        [7, None],
        [13, 0],
        [11, 4],
        [10, 2],
        [1, 0],
    ]
    head = array_to_linked_list(nodes)
    output = linked_list_to_array(Solution().copyRandomList(head))
    print(output)

    # node = head
    # while node:
    #     next_val = node.next.val if node.next else None
    #     random_val = node.random.val if node.random else None
    #     print(node.val, next_val, random_val)
    #     node = node.next

    # output = linked_list_to_array(head)
    # print(f"nodes = {nodes}")
    # print(f"output = {output}")
    pass
