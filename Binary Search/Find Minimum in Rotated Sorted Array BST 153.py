def findMin(nums:List[int])->int:
    N = len(nums)
    start = 0
    end = N -1
    prev = 0
    next = 0

    while(start <= end):
        if(nums[start] <= nums[end]):
            return nums[start]
        mid = start + (end - start)//2
        next = (mid + 1) % N
        prev = (mid + N - 1) % N

        if(nums[mid] <= nums[prev] and nums[mid] <= nums[next]):
            return nums[mid]
        elif(nums[start] <= nums[mid] and nums[mid] >= nums[N-1]):
            start = mid + 1 % N
        else:
            end = mid + N - 1 % N

