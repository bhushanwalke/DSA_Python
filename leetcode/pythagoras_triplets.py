def triplets(arr):
    arr.sort()
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]
    res = []
    for i in range(len(arr)-1, 2, -1):
        l = 0
        r = i-1
        while l < r:
            if arr[l] + arr[r] == arr[i]:
                 res.append((arr[l], arr[r], arr[i]))

            if arr[l] + arr[r] < arr[i]:
                l +=1
            else:
                r -= 1
    return res


print triplets([3,1,4,6,5,11,60,61])
