import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# heapq.heapify(listForTree)             # for a min heap
# heapq._heapify_max(listForTree)        # for a maxheap!!

print listForTree


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums_heap = nums
    heapq._heapify_max(nums_heap)
    for i in range(k-1):
        nums_heap.pop(0)
        heapq._heapify_max(nums_heap)
    return nums_heap.pop(0)


print findKthLargest(listForTree, 2)
