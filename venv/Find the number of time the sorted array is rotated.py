

def findMinIndex( nums, target) -> int:
    print(nums)
    N = len(nums)
    start = 0
    end = N - 1
    prev = 0
    nex = 0

    while (start <= end):
        mid = start + (end - start) // 2
        nex = (mid + 1) % N
        prev = (mid + N - 1) % N

        if (nums[mid] <= nums[prev] and nums[mid] <= nums[nex]):
            return mid
        elif (nums[start] <= nums[mid] and nums[mid] >= nums[N-1]):
            start = mid+1 % N
        else:
            end = (mid + N - 1) % N
    return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    findMinIndex()








