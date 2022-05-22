class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums))

    def binary_search(self, nums, target, left, right):

        while (left < right):
            print('hiii')
            mid = (left + right) // 2

            if (nums[mid] >= target):
                right = mid
            else:
                left = mid + 1
        print(left)
        return left

