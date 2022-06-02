def findTheNumberOfOccurence(nums, target) -> int:
    start = 0
    end = len(nums)-1
    first = -1
    last = -1

    #find the first occurency position
    while(start <= end):
        mid = start + (end - start) //2
        if(nums[mid] == target):
            first = mid
            end = mid -1
        elif target< nums[mid]:
            end = mid-1
        else:
            start = mid +1
    #find the last occurency position
    while(start <= end):
        mid = start + (end - start) //2
        if(nums[mid] == target):
            last = mid
            start = mid + 1
        elif target< nums[mid]:
            end = mid-1
        else:
            start = mid +1

    return (last - first) + 1


