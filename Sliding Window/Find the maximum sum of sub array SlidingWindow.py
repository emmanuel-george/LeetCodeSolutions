def find_max_sum(nums, size, k):
    i = 0
    j = 0
    total = 0
    mx = 0
    while j < size:
        total = total + nums[j]

        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            mx = max(mx, total)
            total = total - nums[i]
            i += 1
            j += 1

    return mx


if __name__ == '__main__':
    nums = [2, 5, 1, 8, 2, 9, 1]
    k = 3
    size = len(nums)
    result = find_max_sum(nums, size, k)
    print(result)
