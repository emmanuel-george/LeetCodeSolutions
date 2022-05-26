# Floor is the Greatest element among the array which is smaller than the element
#nums = [1,2,3,4,8,10,10,17,19]
#element = 5
#possible candidates are 1,2,3,4
# among them the greatest is 4 and hence return 4
def findFloor(nums, element):
    n = len(nums)
    start = 0
    end = n-1
    res = -1
    while(start <= end):
        mid = start + (end -start)//2
        if(nums[mid] == element):
            return nums[mid]
        if(arr[mid]<element):
            res = arr[mid]
            start = mid + 1
        else:
            end = mid - 1

    return res


# Ceil is the Smallest element among the array which is greater than the element
# nums = [1,2,3,4,8,10,10,17,19]
# element = 5
# possible candidates are 8,10,10,17,19
# among them the greatest is 8 and hence return 8
def findCeil(nums, element):
    n = len(nums)
    start = 0
    end = n - 1
    res = -1
    while (start <= end):
        mid = start + (end - start) // 2
        if (nums[mid] == element):
            return nums[mid]
        if (arr[mid] > element):
            res = arr[mid]
            end = mid - 1
        else:
            start = mid + 1
    return res
