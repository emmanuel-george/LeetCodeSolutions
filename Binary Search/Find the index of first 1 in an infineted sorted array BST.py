# first find the index of end in the infinet sored array
# Second from the range obtained from first step find out the first occurence in sorted array

def findEndIndex(nums, element):
    start = 0
    end = start + 1
    ans = []

    while(element > nums[end]):
        start = end
        end = end *2
    ans.append(start)
    ans.append(end)
    return ans

def firstOccurence(nums, element, start, end):
    res = -1

    while start <= end:
        mid = start + (end -start)//2
        if(nums[mid] == element):
            res = mid
            end = mid-1
        elif(nums[mid] > element):
            end = mid - 1
        else:
            start = mid +1
    return res

if __name__ == '__main__':

    #nums = [0,0,0,0,0,0,0,0,,1,1,1,1,1,1,.......... Infinet]
#element = 1
#ans = findEndIndex(nums,element)
#index = firstOccurence(nums, element, ans[0], ans[1])
#return index

