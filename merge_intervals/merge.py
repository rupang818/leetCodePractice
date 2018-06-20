# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Sort the intervals, based on their start
        # 0. if len(intervals) <= 1: return intervals
        # 1. save the first interval's max, maxSoFar
        # 2. if the next element's end <= maxSoFar, skip it
        # 3. else (if the next elemtn's end > maxSoFar)
        #       - if next.start <= curr.end, set curr interval's .end to next elemtn's end
        #       - else: set curr element to next element
        intervals.sort(key=lambda x: x.start)
        
        if len(intervals) <= 1:
            return intervals
        
        currInterval = intervals[0]
        currMax = currInterval.end
        i=1
        while i < len(intervals):
            nextInterval = intervals[i]
            if nextInterval.end > currMax:
                if nextInterval.start <= currMax:
                    currInterval.end = nextInterval.end
                    del intervals[i]
                else:
                    currInterval = nextInterval
                    i+=1
                currMax = currInterval.end
            else:   # nextInterval is a subset of currInterval
                del intervals[i]
        return intervals
        
