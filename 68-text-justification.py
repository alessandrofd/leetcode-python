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
        def select_words(word_index):
            line = []
            words_length = 0
            while (
                word_index < len(words)
                and (words_length + len(line) + len(words[word_index])) <= max_width
            ):
                line.append(words[word_index])
                words_length += len(words[word_index])
                word_index += 1

            return (line, words_length)

        def space_line(line, words_length, last_word):
            num_words = len(line)
            spaces = max_width - words_length - (num_words - 1)

            if num_words == 1 or last_word == len(words):
                return " ".join(line) + " " * spaces

            spacing = spaces // (num_words - 1)
            extra_spaces = spaces % (num_words - 1)

            for i in range(num_words - 1):
                line[i] += " " * spacing

            for i in range(extra_spaces):
                line[i] += " "

            return " ".join(line)

        result = []
        word_index = 0
        while word_index < len(words):
            line, words_length = select_words(word_index)
            word_index += len(line)
            result.append(space_line(line, words_length, word_index))

        return result


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
    output = Solution().fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )

    for line in output:
        print(f"{len(line)}: [{line}]")
