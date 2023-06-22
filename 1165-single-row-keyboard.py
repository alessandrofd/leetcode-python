class Solution_me:
    def calculateTime(self, keyboard, word):
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]] = i

        distance = 0
        position = 0
        for letter in word:
            distance += abs(d[letter] - position)
            position = d[letter]

        return distance


class Solution:
    def calculateTime(self, keyboard, word):
        index = {c: i for i, c in enumerate(keyboard)}
        result = temp = 0
        for char in word:
            result += abs(index[char] - temp)
            temp = index[char]

        return result
