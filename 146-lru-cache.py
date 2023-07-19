"""
Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size
    capacity.

    int get(int key) Return the value of the key if the key exists,
    otherwise return -1.

    void put(int key, int value) Update the value of the key if the key
    exists. Otherwise, add the key-value pair to the cache. If the number of
    keys exceeds the capacity from this operation, evict the least recently
    used key.

The functions get and put must each run in O(1) average time complexity.

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.
"""


class Node:
    def __init__(self, key=None, prev_node=None, next_node=None):
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev_node=self.head)
        self.head.next_node = self.tail

    def push_to_head(self, key):
        node = Node(key, self.head, self.head.next_node)

        node.next_node.prev_node = node
        self.head.next_node = node

        return node

    def move_to_head(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

        node.prev_node = self.head
        node.next_node = self.head.next_node

        node.next_node.prev_node = node
        self.head.next_node = node

    def pop_from_tail(self):
        node = self.tail.prev_node

        node.prev_node.next_node = self.tail
        self.tail.prev_node = node.prev_node

        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.counter = 0
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node, value = self.cache[key]
        self.list.move_to_head(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node, _ = self.cache[key]
            self.list.move_to_head(node)
            self.cache[key] = (node, value)
        else:
            if self.counter == self.capacity:
                node = self.list.pop_from_tail()
                del self.cache[node.key]
                self.counter -= 1

            node = self.list.push_to_head(key)
            self.cache[key] = (node, value)
            self.counter += 1


def test1():
    """test"""

    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    print(lru_cache.capacity, len(lru_cache.cache))
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4


def test2():
    """test"""

    cache2 = LRUCache(2)
    assert cache2.get(2) == -1
    cache2.put(2, 6)
    assert cache2.get(1) == -1
    cache2.put(1, 5)
    cache2.put(1, 2)
    assert cache2.get(1) == 2
    assert cache2.get(2) == 6
