class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if (len(nums) == 1):
            return 0

        while start <= end:
            mid = start + (end - start) // 2
            # First check if mid lies in the range  0+1 and size-2
            if (mid > 0 and mid < len(nums) - 1):
                if (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                    return mid
                elif (nums[mid - 1] > nums[mid]):
                    end = mid - 1
                else:
                    start = mid + 1

            # second if mid is 0
            elif (mid == 0):
                if (nums[0] > nums[1]):
                    return 0
                else:
                    return 1

            # third if mid is in last index
            elif (mid == len(nums) - 1):
                if (nums[len(nums) - 1] > nums[len(nums) - 2]):
                    return len(nums) - 1
                else:
                    return len(nums) - 2
        return -1