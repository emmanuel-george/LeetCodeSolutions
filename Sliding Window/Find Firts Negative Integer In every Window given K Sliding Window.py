from collections import deque


def print_first_negatives(nums, size, k):
    i = 0
    j = 0
    output = []
    Q = deque([])

    while j < size:
        if nums[j] < 0:
            Q.append(nums[j])
        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            if len(Q) == 0:
                output.append(0)
            else:
                output.append(Q[0])
                if nums[i] == Q[0]:
                    Q.popleft()
                i += 1
                j += 1
    print(output)


if __name__ == '__main__':
    nums = [12, -1, -7, 8, -15, 30, 16, 28]
    size = 8
    k = 3
    print_first_negatives(nums, size, k)
