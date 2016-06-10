import sys
def maxsubarraysum(arr, l, h):
    if l == h:

        # print arr[:h]
        return arr[l]

    m = (l+h)/2

    return max(maxsubarraysum(arr, l, m),
               maxsubarraysum(arr, m+1, h),
               maxcrossingsum(arr, l, m, h))

def maxcrossingsum(arr, l,m,h):
    print "maxcross", arr[l:h]
    sum = 0
    left_sum = -sys.maxint
    right_sum = -sys.maxint

    for i in range(m, l, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    sum = 0
    for i in range(m+1, h):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
    tmp = left_sum + right_sum
    return left_sum + right_sum


print maxsubarraysum([-2,-5,6,-2,-3,1,5,-6], 0, 7)
