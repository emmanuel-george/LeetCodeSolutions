# Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.
#
# Example :
#
# Input : pages[] = {12, 34, 67, 90}
#         m = 2
# Output : 113
# Explanation:
# There are 2 number of students. Books can be distributed
# in following fashion :
#   1) [12] and [34, 67, 90]
#       Max number of pages is allocated to student
#       2 with 34 + 67 + 90 = 191 pages
#   2) [12, 34] and [67, 90]
#       Max number of pages is allocated to student
#       2 with 67 + 90 = 157 pages
#   3) [12, 34, 67] and [90]
#       Max number of pages is allocated to student
#       1 with 12 + 34 + 67 = 113 pages
#
# Of the 3 cases, Option 3 has the minimum pages = 113.

def findMinPages(nums, size, noOfStudents):
    start = max(nums)
    end = sum(nums)
    res = -1
    if(size < noOfStudents):
        return -1
    while(start <= end):
        mid = start+(end-start)//2
        if(isValid(nums, size, noOfStudents, mid)):
            res = nums[mid]
            end = mid - 1
        else:
            start = mid + 1
    return res

def isValid(nums, size, noOfStudents, max):
    sum = 0
    student = 1
    for i in range(size):
        sum = sum + nums[i]
        if(sum>max):
            student += 1
            sum = nums[i]
        if(student > noOfStudents):
            return false
    return true




