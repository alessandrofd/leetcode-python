class Solution:
    def reductionOperations(self, nums):
        nums.sort(reverse=True)

        operations = 0
        repeats = 0
        i = 0
        while i < len(nums):
            repeats += 1

            if nums[i] == nums[-1]:
                break

            while nums[i] == nums[i + 1]:
                i += 1
                repeats += 1

            operations += repeats
            i += 1

        return operations

    def reductionOperations_step(self, nums):
        nums.sort()

        operations = 0
        up = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1

            operations += up

        return operations


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        # Solution().reductionOperations_step,
        Solution().reductionOperations
    ]
    # fmt: on

    data = [
        # [[5, 1, 3], 3],
        # [[1, 1, 1], 0],
        [[1, 1, 2, 2, 3], 4],
    ]

    for func in funcs:
        for nums, expected in data:
            assert func(nums) == expected
