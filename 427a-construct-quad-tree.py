"""
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid
with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf
is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly
four children. Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node
    represents a grid of 0's.

    isLeaf: True if the node is leaf node on the tree or False if the node
    has the four children.

Constraints:
    n == grid.length == grid[i].length
    n == 2^x where 0 <= x <= 6
"""


class Node:
    """Definition for a QuadTree node."""

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct_recurseTopDown(self, grid):
        pass

    def construct_recurseBottomUp(self, grid):
        pass


grid = [
    [0, 1],
    [1, 0],
]

grid = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
]

print(Solution().construct_recurseTopDown(grid))
print(Solution().construct_recurseBottomUp(grid))
