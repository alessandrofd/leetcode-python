"""
Implement a SnapshotArray that supports the following interface:

    SnapshotArray(int length) initializes an array-like data structure with
    the given length. Initially, each element equals 0.

    void set(index, val) sets the element at the given index to be equal to val.

    int snap() takes a snapshot of the array and returns the snap_id: the total
    number of times we called snap() minus 1.

    int get(index, snap_id) returns the value at the given index, at the time
    we took the snapshot with the given snap_id

Constraints:
    1 <= length <= 5 * 10^4
    0 <= index < length
    0 <= val <= 10^9
    0 <= snap_id < (the total number of times we call snap())
    At most 5 * 10^4 calls will be made to set, snap, and get.
"""


class SnapshotArray:
    def __init__(self, length: int):
        self.state = {}
        self.snaps = []
        self.changed = False

    def set(self, index: int, val: int) -> None:
        self.state[index] = val
        self.changed = True

    def snap(self) -> int:
        if self.changed or not self.snaps:
            self.changed = False
            self.snaps.append(self.state.copy())
        else:
            self.snaps.append(self.snaps[-1])

        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        return 0


def test_solution1():
    """test"""

    snapshot_arr = SnapshotArray(3)

    snapshot_arr.set(0, 5)
    assert snapshot_arr.snap() == 0

    snapshot_arr.set(0, 6)
    assert snapshot_arr.get(0, 0) == 5


def test_solution2():
    """test"""

    snapshot_arr = SnapshotArray(3)

    snapshot_arr.set(1, 6)

    assert snapshot_arr.snap() == 0
    assert snapshot_arr.snap() == 1

    snapshot_arr.set(1, 19)
    snapshot_arr.set(0, 4)

    assert snapshot_arr.get(2, 1) == 0
    assert snapshot_arr.get(2, 0) == 0
    assert snapshot_arr.get(0, 1) == 0
