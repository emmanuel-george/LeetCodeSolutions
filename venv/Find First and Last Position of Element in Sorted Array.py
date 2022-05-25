class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        first = -1  # for first occurence
        last = -1  # for last occurence
        ans = []  # list for storing first and last occurences

        # Find the first occurence
        while start <= end:

            mid = start + (end - start) // 2
            if (nums[mid] == target):
                first = mid
                end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        ans.append(first)

        start = 0
        end = len(nums) - 1

        # Find the last occurence
        while start <= end:

            mid = start + (end - start) // 2
            if (nums[mid] == target):
                last = mid
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        ans.append(last)
        return ans def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        first = -1 # for first occurence
        last = -1  # for last occurence
        ans = []   # list for storing first and last occurences

        # Find the first occurence
        while start <= end:

            mid = start + (end -start)//2
            if(nums[mid] == target):
                first = mid
                end = mid-1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        ans.append(first)

        start = 0
        end = len(nums) - 1

        # Find the last occurence
        while start <= end:

            mid = start + (end -start)//2
            if(nums[mid] == target):
                last = mid
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        ans.append(last)
        return ans