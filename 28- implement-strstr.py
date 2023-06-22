"""
Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Constraints:
    1 <= haystack.length, needle.length <= 10^4
    haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr_slidingWindow(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : len(needle) + i] == needle:
                return i
        return -1


funcs = [Solution().strStr_slidingWindow]
data = [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1), ("leetcode", "code", 4)]

for haystack, needle, output in data:
    print(f"haystack = {haystack}, needle = {needle}, Output = {output}")
    for func in funcs:
        print(f"{func.__name__} = {func(haystack, needle)}")
    print()
