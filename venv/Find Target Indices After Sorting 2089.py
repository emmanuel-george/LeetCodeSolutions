def binary_search( nums, target, left, right):
    # nums.sort()  # sorting array
    # return list(range(bisect_left(nums, target), bisect_right(nums, target)))
    # # return range from left most occurrence to rightmost occurrence

    left_position, right_position = -1, -1
    ans = []

    # for finding left position in the list
    while (left < right):
        mid = (left + right) // 2
        if (nums[mid] >= target):
            right = mid

        else:
            left = mid + 1

    if (left < len(nums) and nums[left] == target):
        left_position = left

    left, right = 0, len(nums)

    # for finding right most position in the list
    while (left < right):
        mid = (left + right) // 2
        if (nums[mid] <= target):
            left = mid + 1
        else:
            right = mid

    if (nums[right - 1] == target):
        right_position = right - 1

    for i in range(left_position, right_position + 1):
        if (left_position != -1 and right_position != -1):
            ans.append(i)

    return ans

if __name__ == '__main__':
    nums = [1,2,5,2,3]
    target = 2
    res = binary_search(sorted(nums), target, 0, len(nums))
    print(res)
