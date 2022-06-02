def find_maxsize(arr, s):
    summ = 0
    mx = 0
    i, j = 0, 0
    while j < len(arr):
        summ += arr[j]
        if summ < s:
            j += 1
        elif summ == s:
            mx = max(mx, j - i + 1)
            j += 1
        elif summ > s:
            while summ > s:
                summ -= arr[i]
                i += 1
            j += 1
    return mx


if __name__ == '__main__':
    arr = [4, 1, 1, 1, 2, 3, 5]
    s = 5
    print(find_maxsize(arr, s))
