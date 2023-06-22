"""
Given an array of integers nums, sort the array in ascending order and
return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.

Constraints:
    1 <= nums.length <= 5 * 10^4
    -5 * 10^4 <= nums[i] <= 5 * 10^4
"""


class Solution:
    """Solution class"""

    def sortArray_merge(self, nums):  # pylint: disable=invalid-name
        """Merge sort"""
        temp = [0] * len(nums)

        def merge(left, mid, right):
            start1, n1 = left, mid - left + 1
            start2, n2 = mid + 1, right - mid

            for i in range(left, right + 1):
                temp[i] = nums[i]

            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp[start1 + i] <= temp[start2 + j]:
                    nums[k] = temp[start1 + i]
                    i += 1
                else:
                    nums[k] = temp[start2 + j]
                    j += 1
                k += 1

            # Remaining elements
            while i < n1:
                nums[k] = temp[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp[start2 + j]
                j += 1
                k += 1

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)

        merge_sort(0, len(nums) - 1)
        return nums

    def sortArray_heap(self, nums):  # pylint: disable=invalid-name
        """Heap sort"""
        n = len(nums)

        def heapify(n, root):
            # Initialize largest as root
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            # If left child is largest than root
            if left < n and nums[left] > nums[largest]:
                largest = left

            # If right child is larger than largest so far
            if right < n and nums[right] > nums[largest]:
                largest = right

            # If largest is not root, swap root with largest element
            # Recursively heapify the affected subtree
            if largest != root:
                nums[root], nums[largest] = nums[largest], nums[root]
                heapify(n, largest)

        # Build heap; heapify all elements except leaf nodes
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Traverse elements one by one, to move current root to end, and
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            # call max heapify on the reduces heap
            heapify(i, 0)

        return nums

    def sortArray_counting(self, nums):  # pylint: disable=invalid-name
        """Counting sort"""
        count_nums = {}
        max_num = max(nums)
        min_num = min(nums)

        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1

        index = 0
        for num in range(min_num, max_num + 1):
            for _ in range(count_nums.get(num, 0)):
                nums[index] = num
                index += 1

        return nums

    def sortArray_radix(self, nums):  # pylint: disable=invalid-name
        """Radix sort"""

        def bucket_sort(place_value):
            buckets = [[] for _ in range(10)]

            for num in nums:
                digit = (abs(num) // place_value) % 10
                buckets[digit].append(num)

            index = 0
            for digit in range(10):
                for num in buckets[digit]:
                    nums[index] = num
                    index += 1

        max_num = max(map(abs, nums))
        max_digits = len(str(max_num))

        for i in range(max_digits):
            bucket_sort(10**i)

        # Separate negatives and reverse them
        positives = [num for num in nums if num >= 0]
        negatives = [num for num in nums if num < 0]
        negatives.reverse()

        return negatives + positives


data = [[5, 2, 3, 1], [5, 1, 1, 2, 0, 0, -11, -4, -25]]
# Output: [1,2,3,5]
# Output: [0,0,1,1,2,5]

funcs = [
    Solution().sortArray_merge,
    Solution().sortArray_heap,
    Solution().sortArray_counting,
    Solution().sortArray_radix,
]

for nums in data:
    for func in funcs:
        print(func(nums))
