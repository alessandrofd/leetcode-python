"""
Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""

from collections import Counter
from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    def reorganizeString_pq(self, s: str) -> str:
        return ""

    def reorganizeString_arr(self, s: str) -> str:
        return ""


if __name__ == "__main__":
    print(Solution().reorganizeString_arr("ogccckcwmbmxtsbmozli"))
