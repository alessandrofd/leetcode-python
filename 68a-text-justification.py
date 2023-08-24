"""
Given an array of strings words and a width maxWidth, format the text such
that each line has exactly maxWidth characters and is fully (left and right)
justified.

You should pack your words in a greedy approach; that is, pack as many words
as you can in each line. Pad extra spaces ' ' when necessary so that each
line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If
the number of spaces on a line does not divide evenly between words, the
empty slots on the left will be assigned more spaces than the slots on the
right.

For the last line of text, it should be left-justified, and no extra space is
inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space
    characters only.

    Each word's length is guaranteed to be greater than 0 and not exceed
    axWidth.

    The input array words contains at least one word.

Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        return [""]


def test_solution():
    """test"""

    funcs = [
        Solution().fullJustify,
    ]

    # fmt: off
    data = [
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            [
                "This    is    an", 
                "example  of text", 
                "justification.  "
            ],
        ),
        (
            ["What", "must", "be", "acknowledgment", "shall", "be"],
            16,
            [
                "What   must   be", 
                "acknowledgment  ", 
                "shall be        "
            ],
        ),
        (
            [
                "Science", "is", "what", "we", "understand", "well", "enough", 
                "to", "explain", "to", "a", "computer.", "Art", "is", 
                "everything", "else", "we", "do", 
            ],
            20,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
        ),
    ]
    # fmt: on

    for words, max_width, expected in data:
        for func in funcs:
            assert func(words, max_width) == expected


if __name__ == "__main__":
    pass
