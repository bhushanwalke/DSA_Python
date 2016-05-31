'''
Given a set of distinct integers, nums, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
import math

class Solution(object):
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in xrange(1 << len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i >> j & 1: #if i & 1 << j:  #
                    tmp.append(nums[j])
            res.append(tmp)
        return res

s = Solution()
print s.subsets([1,2])

# if __name__ == "__main__":
#     assert Solution().subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
