"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating
characters in chars:

    If the group's length is 1, append the character to s.

    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead,
be stored in the input character array chars. Note that group lengths that
are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of
the array.

You must write an algorithm that uses only constant extra space.

Constraints:
    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit,
    or symbol.
"""


class Solution:
    def compress(self, chars):
        n = len(chars)

        current = 0
        length = 0
        for i in range(n):
            if chars[current] != chars[i]:
                chars[length] = chars[current]
                length += 1
                if i - current > 1:
                    for char in str(i - current):
                        chars[length] = char
                        length += 1
                current = i

        chars[length] = chars[current]
        length += 1
        if current < n - 1:
            for char in str(n - current):
                chars[length] = char
                length += 1

        del chars[length:]

        return length


data = []
data.append(["a", "a", "b", "b", "c", "c", "c"])
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]

data.append(["a"])
# Output: 1, and the first character of the input array should be: ["a"]

data.append(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
# Output: 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].

for chars in data:
    print(Solution().compress(chars), chars)
