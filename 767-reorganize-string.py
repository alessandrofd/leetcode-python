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
        pq = [(-count, letter) for letter, count in Counter(s).items()]
        heapify(pq)

        max_count = pq[0][0] * -1
        if max_count > ceil(len(s) / 2):
            return ""

        result = []
        while pq:
            if len(pq) == 1:
                result.append(pq[0][1])
                break

            first_count, first_letter = heappop(pq)
            second_count, second_letter = heappop(pq)

            result += [first_letter, second_letter]

            if second_count + 1 != 0:
                heappush(pq, (second_count + 1, second_letter))

            if first_count + 1 != 0:
                heappush(pq, (first_count + 1, first_letter))

        return "".join(result)

    def reorganizeString_arr(self, s: str) -> str:
        sorted_freqs = [(count, letter) for letter, count in Counter(s).items()]
        sorted_freqs.sort(reverse=True)

        max_count = sorted_freqs[0][0]
        if max_count > ceil(len(s) / 2):
            return ""

        result = [""] * len(s)
        index = 0
        for count, letter in sorted_freqs:
            while count:
                if index >= len(s):
                    index = 1

                result[index] = letter
                count -= 1
                index += 2

        return "".join(result)


if __name__ == "__main__":
    print(Solution().reorganizeString_arr("ogccckcwmbmxtsbmozli"))
