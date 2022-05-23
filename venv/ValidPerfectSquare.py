

def binarysearch(left, right):
    num = right
    while(left<=right):
        mid = (left + right) //2
        if(mid * mid == num):
            return True
        if(mid * mid > num):
            right = mid -1
        else:
            left = mid + 1
    if(left * left == num):
        return True
    else:return False




if __name__ == '__main__':
    num = 16
    result = binarysearch(1,16)
    print(result)
