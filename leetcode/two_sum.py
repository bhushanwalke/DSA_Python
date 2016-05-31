def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map = {}
    if len(nums) <= 1:
        return nums
    for i in range(0, len(nums)):
        numToFind = target - nums[i]

        if hash_map.has_key(numToFind):
            return [hash_map[numToFind], i]
        hash_map[nums[i]] = i

print twoSum([2,7,5,6,8,9], 9)
