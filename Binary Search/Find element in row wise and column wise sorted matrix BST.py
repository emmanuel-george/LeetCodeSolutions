def findElement(mat, n, m, x):
    i = 0
    j = m-1
    ans = []

    while(i>=0 and i<n and j>=0 and j<m):
        if(mat[i][j] == x):
            ans.append(i)
            ans.append(j)
            return ans
        elif(mat[i][j]>x):
            j -= 1
        elif(mat[i][j]<x):
            i += 1
    return [-1,-1]

if __name__ == '__main__':
    mat = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
    res = findElement(mat,4,4,7)
    print('res[0] is '+str(res[0]))
    print('res[1] is '+str(res[1]))
    print('The element is '+str(mat [res[0]] [res[1]]))

