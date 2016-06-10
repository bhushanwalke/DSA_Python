def longestseries(arr):
    maxc = 1
    for i in arr:
        left = i-1
        right = i+1
        count = 1
        arr.remove(i)
        while(left in arr):
            count += 1
            tmpl = left
            arr.remove(left)
            left = tmpl - 1

        while(right in arr):
            count += 1
            tmpr = right
            arr.remove(right)
            right = tmpr - 1

        maxc = max(maxc, count)

    return maxc





print longestseries([10,2,5,3,4,9])
