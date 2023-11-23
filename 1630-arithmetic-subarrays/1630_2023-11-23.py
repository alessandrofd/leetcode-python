class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        result = []

        for left, right in zip(l, r):
            if (left == right) or (left + 1 == right):
                result.append(True)
                continue

            sub_array = nums[left : right + 1]
            min_num = min(sub_array)
            max_num = max(sub_array)

            if (max_num - min_num) % (len(sub_array) - 1) != 0:
                result.append(False)
                continue

            diff = (max_num - min_num) // (len(sub_array) - 1)

            if diff == 0:
                result.append(True)
                continue

            num_set = set(sub_array)
            is_arithmetic_sequence = True
            for j in range(len(num_set)):
                if min_num + j * diff not in num_set:
                    is_arithmetic_sequence = False
                    break
            result.append(is_arithmetic_sequence)

        return result

    def checkArithmeticSubarrays_sort(self, nums, l, r):
        def is_arithmetic_sequence(nums):
            nums.sort()
            diff = nums[1] - nums[0]
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] != diff:
                    return False
            return True

        result = []

        for left, right in zip(l, r):
            result.append(is_arithmetic_sequence(nums[left : right + 1]))

        return result


def test_solution():
    """test solution"""

    funcs = [
        Solution().checkArithmeticSubarrays,
        Solution().checkArithmeticSubarrays_sort,
    ]

    data = [
        [
            [4, 6, 5, 9, 3, 7],
            [0, 0, 2],
            [2, 3, 5],
            [True, False, True],
        ],
        [
            [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
            [0, 1, 6, 4, 8, 7],
            [4, 4, 9, 7, 9, 10],
            [False, True, False, False, True, True],
        ],
    ]

    for func in funcs:
        for nums, l, r, expected in data:
            assert func(nums, l, r) == expected
