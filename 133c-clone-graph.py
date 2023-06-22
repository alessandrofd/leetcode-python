"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and
so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent
a finite graph. Each list describes the set of neighbors of a node in
the graph.

The given node will always be the first node with val = 1. You must return
the copy of the given node as a reference to the cloned graph.

Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from
    the given node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph_dfs(self, node):

    def cloneGraph_bfs(self, root):
