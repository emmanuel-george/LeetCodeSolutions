#nums = [1,2,3,4,5,6,7..........Infinite
#element = 7
#Steps 1) First find the high index then apply Binary Search

def findEndIndex(nums, element):
    start = 0
    end = start +1
    res = []

    while(element > nums[end]):
        start = end
        end = end  * 2
    res.append(start)
    res.append(end)
    return res

def binarySearch(nums, element, startIndex, endIndex):

    start = startIndex
    end = endIndex

    while start <= end:
        mid = start + ( end - start) //2
        if(nums[mid] == element):
            return nums[mid]
        if(nums[mid] > element):
            end = mid -1
        else:
            start = mid +1
    return -1

if __name__ == '__main__':

# nums = [1,2,3,4,5,6,7..........Infinite
# element = 7
# res = findEndIndex(nums, element)
# answer = binarySearch(nums, element, res[0], res[1]


