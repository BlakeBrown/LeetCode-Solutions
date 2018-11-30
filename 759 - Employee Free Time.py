# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        mergedWorkingTimes = self.mergeWorkingTimes(schedule)
        return self.findFreeTime(mergedWorkingTimes)
        
    # Merges all working times together
    def mergeWorkingTimes(self, schedule):
        workingTimes = []
        for worker in schedule:
            for interval in worker:
                workingTimes.append(interval)
        workingTimes = self.mergeIntervals(workingTimes)
        return workingTimes
    
    # See LeetCode #56 - Merge Intervals
    def mergeIntervals(self, intervals):
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

    # Finds free time, the gaps between working times
    def findFreeTime(self, workingTimes):
        if len(workingTimes) <= 1:
            return []
        gaps = []
        for i in range(0, len(workingTimes)-1):
            gaps.append(Interval(workingTimes[i].end, workingTimes[i+1].start))
        return gaps