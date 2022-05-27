def findPeakPos(nums):
    start = 0
    end = len(nums) - 1

    while (start <= end):
        mid = start + (end - start) // 2
        if (mid > 0 and mid < len(nums) - 1):
            if (nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]):
                return mid
            elif (nums[mid - 1] > nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        elif (mid == 0):
            if (nums[0] > nums[1]):
                return 0
            else:
                return 1
        elif (mid == len(nums) - 1):
            if (nums[len(nums) - 1] > nums[len(nums - 2)]):
                return len(nums) - 1
            else:
                return len(nums) - 2
    return -1


def binarySearchAsc(nums, target, start, end):
    while (start <= end):
        mid = start + (end - start) // 2
        if (nums[mid] == target):
            return nums[mid]
        elif (nums[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binarySearchDsc(nums, target, start, end):
    while (start <= end):
        mid = start + (end - start) // 2
        if (nums[mid] == target):
            return nums[mid]
        elif (nums[mid] > target):
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == '__main__':
    nums= [1,3,8,12,4,2]
    target = 4
    index = findPeakPos(nums)
    print('index = '+ str(index))
    res1 = binarySearchAsc(nums, target,0, index-1)
    res2 = binarySearchDsc(nums, target, index, len(nums)-1)
    print('res1 = ' + str(res1))
    print('res2 = ' + str(res2))
    if(res1 != -1):
        print('The Element is '+str(res1))
    elif (res2 != -1):
        print('The Element is ' + str(res2))
    else:
        print('The element is not found')

