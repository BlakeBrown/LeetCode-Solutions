# Solution 1: Sort the intervals by start time and then merge any overlapping intervals.

# Although it appears this solution takes O(nlogn) time, if you code it by
# using intervals.pop() it actually takes O(n^2).

# This is because removing an element from an array takes O(n) time in the worst case.
# Careful!!

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i = 1
        while i < len(intervals):
            start1 = intervals[i-1].start
            end1 = intervals[i-1].end
            start2 = intervals[i].start
            end2 = intervals[i].end
            if start2 <= end1:
                intervals.pop(i)
                intervals[i-1].end = max(end1,end2)
            else:
                i += 1
        return intervals


# Solution 2: Let's get rid of intervals.pop()
# Use O(n) extra space to store merged intervals, reduces runtime complexity to O(nlogn)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x:x.start)
        merged = [intervals[0]]
        for interval in intervals:
            if interval.start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, interval.end)
            else:
                merged.append(interval)
        return merged