def find_maximums_in_contigious_subarray(nums, k):
    ans = []  # for storing answer
    # Check if k is greater than array
    if k > len(nums):
        ans.append(max(nums))
        return ans
    i, j = 0, 0
    max_list = []

    while j < len(nums):
        # removing the smallest elements in the list which are smaller than nums[j]
        while max_list and max_list[-1] < nums[j]:
            max_list.pop()

        max_list.append(nums[j])

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            # The first element in max list is always the largest element hence append
            ans.append(max_list[0])
            # Removing calculations for ith index before incrementing i and j value
            if max_list[0] == nums[i]:
                max_list.pop(0)
            i += 1
            j += 1
    return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(find_maximums_in_contigious_subarray(nums, k))
