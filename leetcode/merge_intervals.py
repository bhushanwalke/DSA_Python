# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

intervals = []

I1 = Interval(1,4)
intervals.append(I1)
I2 = Interval(0,2)
intervals.append(I2)
I3 = Interval(3,5)
intervals.append(I3)
I4 = Interval(9,18)
intervals.append(I4)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        res.append(intervals[0])
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in intervals:
            print [i.start, i.end]
        if len(intervals) < 1:
            return res
        i = 1
        while i < len(intervals):
            if res[-1].end >= intervals[i].start:
                res[-1].end = max(intervals[i].end, res[-1].end)
                i+=1
            else:
                res.append(intervals[i])
                i+=1
        return res


    def merge1(self, intervals):
        res = []
        intervals.sort(key=lambda x: x.start)
        inter_len = len(intervals)
        if inter_len < 1:
            return res

        for i in intervals:
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)

        return res



s = Solution()
res1 = s.merge(intervals)
res = s.merge1(intervals)

for i in res1:
    print [i.start, i.end]
