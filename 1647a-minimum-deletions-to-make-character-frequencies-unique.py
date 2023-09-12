"""
A string s is called good if there are no two different characters in s that
have the same frequency.

Given a string s, return the minimum number of characters you need to delete
to make s good.

The frequency of a character in a string is the number of times it appears in
the string. For example, in the string "aab", the frequency of 'a' is 2,
while the frequency of 'b' is 1.

Constraints:
    1 <= s.length <= 10^5
    s contains only lowercase English letters.
"""

from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def minDeletions_duplicates(self, string):
        """Set"""
        count_letters = Counter(string)
        unique_freqs = set()

        deletes = 0
        for freq in count_letters.values():
            while freq and freq in unique_freqs:
                freq -= 1
                deletes += 1
            unique_freqs.add(freq)

        return deletes

    def minDeletions_priority_queue(self, string):
        """Priority Queue"""
        freqs_by_letters = Counter(string)
        heap = list(map(lambda x: x * -1, freqs_by_letters.values()))
        heapify(heap)

        deletes = 0
        while heap:
            largest_freq = heappop(heap)
            if heap and largest_freq == heap[0]:
                if largest_freq < -1:
                    heappush(heap, largest_freq + 1)
                deletes += 1

        return deletes

    def minDeletions_sorting(self, s):
        """Sorting"""
        freqs_by_letters = Counter(s)
        sorted_freqs = sorted(freqs_by_letters.values(), reverse=True)

        total_deletes = 0
        for i in range(1, len(sorted_freqs)):
            if sorted_freqs[i] >= sorted_freqs[i - 1]:
                deletes = min(
                    sorted_freqs[i], sorted_freqs[i] - sorted_freqs[i - 1] + 1
                )
                sorted_freqs[i] -= deletes
                total_deletes += deletes

        return total_deletes


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().minDeletions_duplicates,
        Solution().minDeletions_priority_queue,
        Solution().minDeletions_sorting,
    ]

    data = [
        ['aab', 0],
        ['aaabbbcc', 2],
        ['ceabaacb', 2],
        ['bbcebab', 2],
        ["abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz", 276],
    ]
    # fmt: on

    for string, expected in data:
        for func in funcs:
            assert func(string) == expected


if __name__ == "__main__":
    pass
