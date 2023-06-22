"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to
    contain all positive integers.

    int popSmallest() Removes and returns the smallest integer contained in
    the infinite set.

    void addBack(int num) Adds a positive integer num back into the infinite
    set, if it is not already in the infinite set.

Constraints:
    1 <= num <= 1000
    At most 1000 calls will be made in total to popSmallest and addBack.
"""

from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.enqueued = set()
        self.smallest = 1

    def popSmallest(self):
        if self.heap:
            if self.heap[0] <= self.smallest:
                if self.heap[0] == self.smallest:
                    self.smallest += 1
                self.enqueued.remove(self.heap[0])
                return heappop(self.heap)

        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num):
        if num < self.smallest and num not in self.enqueued:
            heappush(self.heap, num)
            self.enqueued.add(num)


def test_solution():
    """test"""

    obj = SmallestInfiniteSet()
    obj.addBack(2)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 2
    assert obj.popSmallest() == 3
    obj.addBack(1)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 4
    assert obj.popSmallest() == 5
