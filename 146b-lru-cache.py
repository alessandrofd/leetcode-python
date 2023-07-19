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

class LRUCache:
    def __init__(self, capacity: int):

    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:


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
