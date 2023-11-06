from heapq import heappush, heappop, heapify
from sortedcontainers import SortedSet


class SeatManager_heap:
    def __init__(self, n: int):
        self.available_seats = list(range(1, n + 1))
        heapify(self.available_seats)

    def reserve(self) -> int:
        return heappop(self.available_seats)

    def unreserve(self, seat_number: int) -> None:
        heappush(self.available_seats, seat_number)


class SeatManager_heap_no_init:
    def __init__(self, n: int):
        self.marker = 0
        self.available_seats = []

    def reserve(self) -> int:
        if self.available_seats:
            return heappop(self.available_seats)

        self.marker += 1
        return self.marker

    def unreserve(self, seat_number: int) -> None:
        heappush(self.available_seats, seat_number)


class SeatManager:
    def __init__(self, n: int):
        self.marker = 0
        self.available_seats = SortedSet()

    def reserve(self) -> int:
        if self.available_seats:
            return self.available_seats.pop(0)

        self.marker += 1
        return self.marker

    def unreserve(self, seat_number: int) -> None:
        self.available_seats.add(seat_number)
