from random import randrange


class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)

        result = []
        for i in range(n):
            if nums[i][i] == "0":
                result.append("1")
            else:
                result.append("0")

        return "".join(result)

    def findDifferentBinaryString_random(self, nums):
        integers = {int(num, 2) for num in nums}

        n = len(nums)
        result = 0
        while result in integers:
            result = randrange(2**n)

        return f"{result:0={n}b}"

    def findDifferentBinaryString_integers(self, nums):
        integers = {int(num, 2) for num in nums}

        n = len(nums)
        for i in range(n + 1):
            if i not in integers:
                return f"{i:0={n}b}"

        return -1

    def findDifferentBinaryString_recursion(self, nums):
        n = len(nums)
        nums_set = set(nums)

        def generate(num):
            if len(num) == n:
                if num in nums_set:
                    return ""
                return num

            add_zero = generate(num + "0")
            if add_zero:
                return add_zero

            return generate(num + "1")

        return generate("")


def test_solution():
    """test"""

    funcs = [
        Solution().findDifferentBinaryString,
        Solution().findDifferentBinaryString_random,
        Solution().findDifferentBinaryString_integers,
        Solution().findDifferentBinaryString_recursion,
    ]

    # fmt: off
    data = [
        [['01', '10'], ['00', '11']],
        [['00', '01'], ['10', '11']],
        [['111', '011', '001'], ['000', '010', '100', '110', '101']],
    ]
    # fmt: on

    for func in funcs:
        for nums, expected in data:
            assert func(nums) in expected
