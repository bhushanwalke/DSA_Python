import collections
from collections import deque

def maxSlidingWindow(nums, k):
    dq = collections.deque()
    ans = []
    for i in range(len(nums)):
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans

print maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
