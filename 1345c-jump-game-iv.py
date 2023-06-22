"""
Given an array of integers arr, you are initially positioned at the first
index of the array.

In one step you can jump from index i to index:
    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Constraints:
    1 <= arr.length <= 5 * 10^4
    -10^8 <= arr[i] <= 10^8
"""
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pass


data = [
    ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3),
    ([7], 0),
    ([7, 6, 9, 6, 9, 6, 9, 7], 1),
]


funcs = [Solution().minJumps]

for arr, output in data:
    print(f"arr = {arr}\nOutput = {output}")
    for func in funcs:
        print(f"{func.__name__} = {func(arr)}")
