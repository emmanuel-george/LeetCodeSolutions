# array = 1 3 2 4
# Find the nearest greater to the right
# Outout = 3 4 4 -1

def findNearestLargest(array):
    res = []
    stack = []
    i = len(array) - 1

    while i >= 0:
        if not stack:
            res.append(-1)
        elif len(stack) > 0 and stack[-1] > array[i]:
            res.append(array[i])
        elif len(stack) > 0 and stack[-1] <= array[i]:
            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(array[i])
        i -= 1
    return res.reverse()
