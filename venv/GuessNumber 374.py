def guessNumber(self, n: int) -> int:
    return self.binary_search(0, n)


def binary_search(self, start, end):
    if (start > end):
        return -1
    mid = (start + end) // 2

    if (guess(mid) == 0):
        return mid

    if (guess(mid) == 1):
        start = mid + 1

    else:
        end = mid - 1

    return self.binary_search(start, end)

