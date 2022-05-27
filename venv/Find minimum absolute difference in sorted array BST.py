def findMinDifference(nums, element):
    start = 0
    end = len(nums) - 1
    while (start <= end):
        mid = start + (end - start) // 2
        if (nums[mid] == element):
            return nums[mid]
        if (nums[mid] > element):
            end = mid - 1
        else:
            start = mid + 1
    return min(abs(element - nums[start]), abs(element - nums[end]))

if __name__ == '__main__':
    nums = [1,3, 8, 10,11, 15]
    element = 12
    print(str(findMinDifference(nums, element)))
