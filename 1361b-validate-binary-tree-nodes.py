"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two
children left_children[i] and right_children[i], return true if and only if all the
given nodes form exactly one valid binary tree.

If node i has no left child then left_children[i] will equal -1, similarly for
the right child.

Note that the nodes have no values and that we only use the node numbers in
this problem.

Constraints:
    n == left_children.length == right_children.length
    1 <= n <= 10^4
    -1 <= left_children[i], right_children[i] <= n - 1

Topics: Tree, Depth-First Search, Breadth-First Search, Union Find, Graph,
Binary Tree

Hints:
    Find the parent of each node.

    A valid tree must have nodes with only one parent and exactly one node
    with no parent.

Overview:

Before we go into the approaches, let's first talk about what makes a binary
tree valid.

    Obs: Note that while this is not a formal definition of a binary tree,
    these rules are sufficient for solving the problem.

    1.  A binary tree must have a root. This is a node with no incoming edges-
        that is, the root has no parent.

    2.  Every node other than the root must have exactly one parent.

    3. The tree must be connected - every node must be reachable from one node
        (the root).

    4.  There cannot be a cycle.

To solve this problem, we can check the nodes given to us against these rules.

    You may notice that some of these rules imply each other. For example, if
    a binary tree had a root, it would have a cycle only if there was a node
    with more than one parent.
"""

from collections import deque


class Solution:
    def validateBinaryTreeNodes_dfs(
        self, n: int, left_children: list[int], right_children: list[int]
    ) -> bool:
        """
        Approach 1: Depth First Search (DFS)

        One way to solve this problem would be to perform a DFS on the tree and
        check that all the rules are followed. Before we can start a DFS, we need
        to locate the root. Let's define a function findRoot that helps us find the
        root.

        As mentioned above, the root has no parent - this also means that the root
        is not the child of any nodes. The input arrays left_children and right_children
        describe all children, so the root would not appear in these arrays. We can
        simply use a for loop from 0 to n - 1 and for each number, check if it is
        present in left_children or right_children. If it's not present in either, then we
        can return it as the root. If we don't find any root, we can return -1.

        To improve efficiency, we will convert left_children and right_children to a set
        for O(1) checks.

        We will start by obtaining root = findRoot(). If root = -1, there is no
        node without a parent, and we can immediately return false as the tree is
        invalid.

        Once we have the root, we can start a DFS from it. We will implement the
        DFS iteratively with a stack. How can we validate the tree? First of all,
        if we see a node multiple times during the DFS, it means a node has
        multiple parents (and there could be a cycle). We will use a set seen that
        keeps track of all the nodes we have seen so far during the traversal. When
        we move to a child, if child is already in seen, we can immediately return
        false since we would be visiting child for the second time.

        Once the DFS finishes, every node we visited will be in seen. If the tree
        is connected, then the length of seen will be equal to n. If
        seen.length != n, it means that some nodes were not visited, and thus the
        tree must be disconnected. Thus, we can return seen.length == n at the end
        of the algorithm.

        This process is sufficient in validating a binary tree:

            1.  If a binary tree does not have a root, then findRoot will return -1.

            2.  If there is a node with more than one parent, then we will detect it
                with seen.

            3.  If the tree is disconnected, then seen will hold less than n nodes
                at the end.

            4.  If there is a cycle, then we will detect it with seen.

        Any other scenario we don't explicitly check for will be caught by some
        other rule. For example, the second rule we stated was:

            Every node other than the root must have exactly one parent.

        You may be thinking: we are explicitly checking the case when a node has
        multiple parents with seen, but what if there is a node with no parent
        other than the root? That is, what if there are multiple roots? In that
        scenario, findRoot would give us the root with the lowest value. We would
        perform a DFS from there, and never reach any of the other roots. Then at
        the end, seen would have less than n nodes.
        """

        return False

    def validateBinaryTreeNodes_bfs(
        self, n: int, left_children: list[int], right_children: list[int]
    ) -> bool:
        return False

    def validateBinaryTreeNodes_union_find(
        self, n: int, left_children: list[int], right_children: list[int]
    ) -> bool:
        """
        Approach 3: Union Find

        A disjoint-set data structure (also called a union–find), is a data
        structure that stores a collection of disjoint (non-overlapping) sets.
        Union-find provides us with the following methods:

            find: Determine which subset a particular element is in. This can be
            used to determine if two elements are in the same subset.

            union: Join two subsets into a single subset.

        Initially, all nodes belong to their own subset. We will iterate over all
        (parent, child) pairs given in left_children and right_children and attempt a union.
        We want to assign the subset of child to the subset of parent. For each
        call to union(parent, child), we can see if the tree is invalid with the
        following checks:

            If find(child) != child, then child must have been assigned a parent
            earlier, and thus child has multiple parents.

            If parent and child already belong to the same subset, then there must
            be a directed path from child to parent as parent must have been
            assigned to the subset of child earlier, and thus there exists a cycle.

        After performing all union operations successfully between parents and
        their children, there should only be one component in the union-find data
        structure. We can track the number of components by subtracting one from
        the count on each successful union operation, and then check whether the
        final count of components is equal to 1.
        """

        return False


def test_solution():
    """test"""

    funcs = [
        Solution().validateBinaryTreeNodes_dfs,
        Solution().validateBinaryTreeNodes_bfs,
        Solution().validateBinaryTreeNodes_union_find,
    ]

    # fmt: off
    data = [
        [4, [1, -1, 3, -1], [2, -1, -1, -1], True],
        [4, [1, -1, 3, -1], [2, 3, -1, -1], False],
        [2, [1, 0], [-1, -1], False],
    ]
    # fmt: on
    for func in funcs:
        for n, left_children, right_children, expected in data:
            assert func(n, left_children, right_children) == expected
