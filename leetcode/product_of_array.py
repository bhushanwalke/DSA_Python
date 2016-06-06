def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    tmp = 1
    l = len(nums)
    res = []

    for i in range(l):
        res.append(tmp)
        tmp = tmp * nums[i]

    tmp = 1
    for i in range(l-1, -1, -1):
        res[i] = res[i] * tmp
        tmp = tmp * nums[i]

    return res

nums = [1,2,3,4]
print productExceptSelf(nums)
