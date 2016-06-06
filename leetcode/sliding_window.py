from collections import deque

def maximumWindow(A, k):
    D = deque()
    res, i = [], 0
    for i in range(len(A)):
        while D and D[-1][0] <= A[i]:
            print D[-1][0]
            D.pop()
        D.append((A[i], i+k-1))
        if i >= k-1:
            res.append(D[0][0])
        if i == D[0][1]:
            print D[0][1]
            D.popleft()
    return res

print maximumWindow([4,3,2,1,5,7,6,8,9], 3)
